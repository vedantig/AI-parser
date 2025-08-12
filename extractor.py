from pathlib import Path
import fitz  # PyMuPDF for PDF files
from docx import Document  # for DOCX files

def extract_text(file_path: Path) -> str:
    """Extract text from a PDF or DOCX file.

    Args:
        file_path: Path to the input document.

    Returns:
        Extracted plain text.

    Raises:
        ValueError: If the file type is unsupported.
    """
    ext = file_path.suffix.lower()
    if ext == ".pdf":
        return _from_pdf(file_path)
    if ext == ".docx":
        return _from_docx(file_path)
    raise ValueError(f"Unsupported file type: {ext}")

def _from_pdf(path: Path) -> str:
    """Extract text from all pages of a PDF."""
    with fitz.open(path) as doc:
        return "\n".join(page.get_text() for page in doc)

def _from_docx(path: Path) -> str:
    """Extract text from all paragraphs of a DOCX."""
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)
