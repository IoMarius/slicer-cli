import numpy as np


def fuse_depth_maps(depths: list[np.ndarray]) -> np.ndarray:
    return np.mean(depths, axis=0)
