import typer
import numpy as np

from slicer.core.preprocess import preprocess
from slicer.core.depth import estimate_depth
from slicer.core.fuse import fuse_depth_maps
from slicer.types.depth_map import DepthMap

from slicer.utils.console import info, success
from slicer.utils.progress import create_progress

app = typer.Typer()


@app.command()
def run(input: list[str]):
    if len(input) > 3:
        raise ValueError("Max 3 images allowed")

    info("Loading images...")

    with create_progress() as progress:
        task = progress.add_task("Processing pipeline", total=3)

        progress.update(task, description="Preprocessing images")
        images = [preprocess(p) for p in input]
        progress.advance(task)

        progress.update(task, description="Estimating depth")
        depths = [estimate_depth(img) for img in images]
        progress.advance(task)

        progress.update(task, description="Fusing depth maps")
        depth = fuse_depth_maps(depths)
        progress.advance(task)

    h, w = depth.shape

    result = DepthMap(
        width=w,
        height=h,
        data=depth.astype(np.float32),
    )

    success("DepthMap generated")
    info(f"Resolution: {w}x{h}")
    info(f"Range: {result.data.min():.3f} → {result.data.max():.3f}")


if __name__ == "__main__":
    app()
