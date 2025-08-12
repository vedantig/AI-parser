from pathlib import Path
from parser.extractor import extract_text

def test_extract_pdf():
    """Test text extraction from a sample PDF file."""
    sample = Path("tests/fixtures/sample.pdf")
    text = extract_text(sample)
    assert isinstance(text, str)
    assert len(text.strip()) > 0

def test_extract_docx():
    """Test text extraction from a sample DOCX file."""
    sample = Path("tests/fixtures/sample.docx")
    text = extract_text(sample)
    assert isinstance(text, str)
    assert len(text.strip()) > 0

def test_unsupported_file_type():
    """Test extraction failure on unsupported file types."""
    fake = Path("tests/fixtures/sample.txt")
    try:
        extract_text(fake)
    except ValueError as e:
        assert "Unsupported file type" in str(e)
    else:
        assert False, "Expected ValueError not raised"
