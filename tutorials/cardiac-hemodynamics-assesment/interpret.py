# interpret.py

import torch
import numpy as np
import neurokit2 as nk
from captum.attr import IntegratedGradients
from scipy.ndimage import binary_dilation


def multimodal_ecg_cxr_attribution(
    last_fold_model,
    last_val_loader,
    sample_idx=0,
    ecg_threshold=0.70,
    cxr_threshold=0.7,
    zoom_range=(3, 3.5),
    lead_number=12,
    sampling_rate=500,
):
    """
    Compute and return all data needed for multimodal ECG+CXR attribution visualization.

    Returns: dict with all tensors, arrays and keys for plotting.
    """
    # Gather all batches (as in your code)
    batches = list(last_val_loader)
    all_xray_images, all_ecg_waveforms, all_labels = [
        torch.cat(items) for items in zip(*batches)
    ]

    # --- Select Sample ---
    xray_image = (
        all_xray_images[sample_idx]
        .unsqueeze(0)
        .to(next(last_fold_model.parameters()).device)
    )
    ecg_waveform = (
        all_ecg_waveforms[sample_idx]
        .unsqueeze(0)
        .to(next(last_fold_model.parameters()).device)
    )
    label = all_labels[sample_idx].item()

    # --- ECG Preprocessing ---
    ecg_waveform_1d = all_ecg_waveforms[sample_idx].cpu().numpy().ravel()
    ecg_smoothed = nk.ecg_clean(ecg_waveform_1d, sampling_rate=sampling_rate)
    ecg_smoothed_tensor = (
        torch.tensor(ecg_smoothed.copy(), dtype=torch.float32)
        .unsqueeze(0)
        .unsqueeze(0)
        .to(next(last_fold_model.parameters()).device)
    )

    # --- Prediction ---
    last_fold_model.eval()
    with torch.no_grad():
        logits = last_fold_model(xray_image, ecg_waveform)
        probabilities = torch.softmax(logits, dim=1)
        predicted_label = torch.argmax(probabilities, dim=1).item()
        predicted_probability = probabilities[0, predicted_label].item()

    # --- Integrated Gradients ---
    integrated_gradients = IntegratedGradients(last_fold_model)
    xray_image.requires_grad_(True)
    ecg_waveform.requires_grad_(True)
    attributions, _ = integrated_gradients.attribute(
        inputs=(xray_image, ecg_smoothed_tensor),
        target=predicted_label,
        return_convergence_delta=True,
    )
    attributions_xray = attributions[0]
    attributions_ecg = attributions[1]

    # --- ECG Attribution ---
    attributions_ecg_np = attributions_ecg.cpu().detach().numpy().squeeze()
    norm_attributions_ecg = (attributions_ecg_np - attributions_ecg_np.min()) / (
        attributions_ecg_np.max() - attributions_ecg_np.min() + 1e-8
    )
    ecg_waveform_np = ecg_smoothed_tensor.cpu().detach().numpy().squeeze()
    full_length = min(60000, len(ecg_waveform_np))
    full_time = np.arange(0, full_length) / sampling_rate / lead_number
    important_indices_full = np.where(
        norm_attributions_ecg[:full_length] >= ecg_threshold
    )[0]

    zoom_start = int(zoom_range[0] * 6000)
    zoom_end = int(zoom_range[1] * 6000)
    zoom_time = np.arange(zoom_start, zoom_end) / sampling_rate / lead_number
    segment_ecg_waveform = ecg_waveform_np[zoom_start:zoom_end]
    segment_attributions = norm_attributions_ecg[zoom_start:zoom_end]
    important_indices_zoom = np.where(segment_attributions >= ecg_threshold)[0]
    zoom_start_sec = zoom_start / sampling_rate / lead_number
    zoom_end_sec = zoom_end / sampling_rate / lead_number

    # --- CXR Attribution: Points ---
    attributions_xray_np = attributions_xray.cpu().detach().numpy().squeeze()
    norm_attributions_xray = (attributions_xray_np - np.min(attributions_xray_np)) / (
        np.max(attributions_xray_np) - np.min(attributions_xray_np) + 1e-8
    )
    xray_image_np = xray_image.cpu().detach().numpy().squeeze()

    binary_mask = norm_attributions_xray >= cxr_threshold
    dilated_mask = binary_dilation(binary_mask, iterations=1)
    y_pts, x_pts = np.where(dilated_mask)
    importance_pts = norm_attributions_xray[y_pts, x_pts]

    return {
        "label": label,
        "predicted_label": predicted_label,
        "predicted_probability": predicted_probability,
        "ecg_waveform_np": ecg_waveform_np,
        "full_time": full_time,
        "full_length": full_length,
        "important_indices_full": important_indices_full,
        "segment_ecg_waveform": segment_ecg_waveform,
        "zoom_time": zoom_time,
        "important_indices_zoom": important_indices_zoom,
        "zoom_start_sec": zoom_start_sec,
        "zoom_end_sec": zoom_end_sec,
        "xray_image_np": xray_image_np,
        "x_pts": x_pts,
        "y_pts": y_pts,
        "importance_pts": importance_pts,
        "ecg_threshold": ecg_threshold,
        "cxr_threshold": cxr_threshold,
    }
