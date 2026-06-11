# slicer-cli

**Python 3.14+** CLI tool — slices images by depth into CNC cutter-ready paths.

## Toolchain

- **Package manager:** `uv` (not pip). Install deps: `uv sync`. Add deps: `uv add <pkg>`.
- **Build backend:** setuptools with `src/` layout (`pyproject.toml` configures `package-dir = {"" = "src"}`).
- **No linter, formatter, type checker, or test framework configured.**
- **No CI/CD** (no `.github/`).
- Editable install via `uv pip install -e .` — `slicer_cli.egg-info/` is a build artifact, do not commit.

## Run

```bash
uv run python -m slicer.cli.main run <image_paths...>
```

Accepts 1–3 image paths. Pipeline: `preprocess → estimate_depth → fuse`.

## Project structure

```
src/slicer/
  cli/main.py       — Typer CLI entrypoint (single `run` command)
  core/
    preprocess.py   — load → resize → normalize
    depth.py        — naive grayscale depth (stub, replace with ML later)
    fuse.py         — mean fusion of depth maps
  types/
    depth_map.py    — DepthMap dataclass (width, height, data: np.ndarray)
  utils/
    image.py        — cv2 imread, resize, normalize (BGR→RGB, float32 /255)
    console.py      — Rich console helpers
    progress.py     — Rich progress bar (SpinnerColumn, BarColumn)
```

## Dependencies (key)

- **typer** — CLI framework
- **opencv-python** — image I/O and resize (`cv2.imread`, `cv2.resize`)
- **numpy** — array operations
- **rich** — terminal UI (progress bars, colored output)
- **scikit-image**, **shapely**, **pillow** — declared but unused in current code
