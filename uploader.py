from pathlib import Path

MAX_SIZE = 10 * 1024 * 1024  # 10 MB

def validate(path: Path) -> Path:
    """Check if file exists, is supported (.pdf/.docx), and within size limit.

    Args:
        path: Path to input file.

    Returns:
        The same path if valid.

    Raises:
        FileNotFoundError: If file doesn't exist.
        ValueError: If file type is unsupported or too large.
    """
    if not path.exists():
        raise FileNotFoundError(f"No such file: {path}")
    if path.suffix.lower() not in (".pdf", ".docx"):
        raise ValueError(f"Unsupported file type: {path.suffix}")
    if path.stat().st_size > MAX_SIZE:
        raise ValueError(f"File too large: {path.stat().st_size} bytes")
    return path
