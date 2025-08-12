from parser.info_parser import parse_all

TEXT = """
Report Title
Report Subtitle

Date: 2025-05-27

Description:
This is a test description.

Name: Alice Example
Email: alice@example.com
Phone: +1 234-567-8901
"""

def test_parse_all():
    """Should extract all expected fields from sample text."""
    data = parse_all(TEXT)

    assert data["title"]       == "Report Title"
    assert data["subtitle"]    == "Report Subtitle"
    assert data["date"]        == "2025-05-27"
    assert data["description"] == "This is a test description."
    assert data["person_name"] == "Alice Example"
    assert data["email"]       == "alice@example.com"
    assert data["phone"]       == "+1 234-567-8901"
