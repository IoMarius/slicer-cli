from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn


def create_progress():
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
    )