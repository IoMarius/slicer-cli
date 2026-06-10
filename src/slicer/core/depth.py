import numpy as np


def estimate_depth(image: np.ndarray) -> np.ndarray:
    """
    Stub depth model.
    Replace later with real ML model.
    """

    gray = image.mean(axis=2)

    depth = (gray - gray.min()) / (gray.max() - gray.min() + 1e-6)

    return depth.astype(np.float32)
