import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils._param_validation import validate_params, Interval, Integral
from nilearn.connectome import vec_to_sym_matrix
import numpy as np

sns.set_theme(style="whitegrid", font_scale=1.5)


@validate_params(
    {
        "values": ["array-like"],
        "ncols": [Interval(Integral, 1, None, closed="left")],
        "figsize": [tuple],
    },
    prefer_skip_nested_validation=False,
)
def plot_phenotypic_distribution(*values, ncols=2, figsize=(16, 20), title=None):
    """
    Plot distribution of phenotypic variables in a grid layout.

    Parameters
    ----------
    *values : tuple of (str, array-like[, str])
        Each tuple should contain a title (str), a value (array-like),
        and optionally a dtype (e.g., "category", "double") to cast the value.

    ncols : int, default=2
        Number of columns in the subplot grid.

    figsize : tuple of int, default=(16, 20)
        Size of the entire figure.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The matplotlib figure object.

    axs : numpy.ndarray of matplotlib.axes.Axes
        The array of subplot axes.

    Notes
    -----
    - Categorical variables are plotted as count plots.
    - Numeric variables are plotted as histograms with KDE.
    """
    if len(values) == 0:
        raise ValueError("At least one value must be provided for plotting.")

    nrows = len(values) // ncols + (len(values) % ncols > 0)
    fig, axs = plt.subplots(
        figsize=figsize,
        nrows=nrows,
        ncols=ncols,
        constrained_layout=True,
    )

    fig.suptitle(title, fontsize=18)

    axs = axs.flatten() if len(values) > 1 else [axs]

    hue = None
    for i, (ax, item) in enumerate(zip(axs, values)):
        # Unpack title, value, optional dtype
        if isinstance(item, tuple):
            if len(item) == 3:
                title, value, dtype = item
                value = pd.Series(value, name=title).astype(dtype)
            else:
                title, value = item
                value = pd.Series(value, name=title)
        else:
            value = item if isinstance(item, pd.Series) else pd.Series(item)
            title = value.name or f"Feature {i+1}"

        value = value.reset_index(drop=True)

        # Check for hue
        if i == 0 and pd.api.types.is_categorical_dtype(value):
            hue = value

        # Plot based on dtype
        use_hue = hue if i > 0 else None
        hue_order = hue.value_counts().index if i > 0 else None
        if value.dtype == "object" or pd.api.types.is_categorical_dtype(value):
            sns.countplot(
                x=value,
                order=value.value_counts().index,
                hue=use_hue,
                hue_order=hue_order,
                ax=ax,
            )
        else:
            sns.histplot(
                x=value, bins=20, kde=True, hue=use_hue, hue_order=hue_order, ax=ax
            )

        ax.set_xlabel(value.name)
        if i % ncols == 0:
            ax.set_ylabel("Number of subjects")
        else:
            ax.set_ylabel(None)
        ax.set_title(f"{title} Distribution")

    return fig, axs


@validate_params(
    {
        "fc": ["array-like"],
        "labels": ["array-like"],
        "title": [str, None],
        "figsize": [tuple],
        "annotate": ["boolean"],
    },
    prefer_skip_nested_validation=False,
)
def plot_connectivity_matrix(
    fc, labels, title=None, figsize=(12, 12), annotate=False, **kwargs
):
    """
    Plot a functional connectivity matrix as a heatmap.

    Parameters
    ----------
    fc : ndarray of shape (n, n) or (n*(n-1)/2,)
        Functional connectivity matrix. Can be a square 2D matrix or a
        vectorized upper triangle.

    labels : list of str
        Labels for each ROI (region of interest). Must match `fc.shape[0]`
        if `fc` is 2D.

    title : str, optional
        Title for the plot.

    figsize : tuple of int, default=(12, 12)
        Size of the matplotlib figure.

    annotate : bool, default=False
        If True, show labels on x and y axes.

    **kwargs : dict
        Additional keyword arguments passed to `sns.heatmap`.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The matplotlib figure object.

    axs : matplotlib.axes.Axes
        The axes on which the heatmap is plotted. The left and right axes
        shows the full and upper triangle of the connectivity matrix,
        respectively.

    Raises
    ------
    ValueError
        If the dimensions of `fc` or its length do not match the expected
        size based on `labels`.
    """
    if fc.ndim not in {1, 2}:
        raise ValueError(
            "Functional connectivity matrix must be 2D or 3D square matrix."
        )

    if fc.ndim == 2 and fc.shape[0] != len(labels):
        raise ValueError(
            "If fc is 2D, its first dimension must match the number of labels."
        )

    if fc.ndim == 1:
        try:
            fc = vec_to_sym_matrix(fc, np.zeros(len(labels)))
        except ValueError as e:
            raise ValueError(
                "The vectorized FC length must be equal to n*(n-1)/2"
            ) from e

    fig, axs = plt.subplots(
        figsize=figsize, ncols=2, gridspec_kw={"width_ratios": [1, 1], "wspace": 0.02}
    )
    fig.suptitle(title)

    vmin = kwargs.get("vmin", np.min(fc))
    vmax = kwargs.get("vmax", np.max(fc))

    # Left plot
    sns.heatmap(
        fc,
        xticklabels=False,
        yticklabels=False,
        square=True,
        ax=axs[0],
        cbar=False,
        vmin=vmin,
        vmax=vmax,
        **kwargs,
    )
    axs[0].set_title("Full Connectivity Matrix")

    # Right plot
    sns.heatmap(
        np.triu(fc, k=1),
        xticklabels=False,
        yticklabels=False,
        square=True,
        ax=axs[1],
        cbar=False,
        vmin=vmin,
        vmax=vmax,
        **kwargs,
    )
    axs[1].set_title("Upper Triangle of Connectivity Matrix")

    # Add shared colorbar to the right of both subplots
    im = axs[1].get_children()[0]  # Get the QuadMesh image
    cbar = fig.colorbar(im, ax=axs, orientation="vertical", fraction=0.02, pad=0.02)
    cbar.ax.tick_params(labelsize=12)

    if annotate:
        # Left: add both x and y tick labels
        axs[0].set_xticks(np.arange(len(labels)))
        axs[0].set_xticklabels(labels, rotation=90, fontsize=10)
        axs[0].set_yticks(np.arange(len(labels)))
        axs[0].set_yticklabels(labels, fontsize=10)

        # Right: remove all tick labels (to save space)
        axs[1].set_xticks(np.arange(len(labels)))
        axs[1].set_xticklabels(labels, rotation=90, fontsize=10)

    return fig, axs
