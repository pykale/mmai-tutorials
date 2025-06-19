#Remap model parameters from the pre-trained checkoints to adjust with new parameter name.

def remap_state_dict_keys(state_dict):
    mapping = [
        ("ecg_encoder.", "signal_encoder."),
        ("ecg_decoder.", "signal_decoder."),
        ("fc_logvar", "fc_log_var"),
        ("signal_encoder.fc_logvar.weight", "signal_encoder.fc_log_var.weight"),
        ("signal_encoder.fc_logvar.bias", "signal_encoder.fc_log_var.bias"),
    ]
    new_state_dict = {}
    for k, v in state_dict.items():
        for old, new in mapping:
            if old in k:
                k = k.replace(old, new)
        new_state_dict[k] = v
    return new_state_dict