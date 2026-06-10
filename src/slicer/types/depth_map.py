from dataclasses import dataclass
import numpy as np


@dataclass
class DepthMap:
    width: int
    height: int
    data: np.ndarray  # (H, W) float32 [0..1]
