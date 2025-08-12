import re
from typing import Dict

# Precompiled patterns
EMAIL = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
PHONE = re.compile(r'\+?\d[\d\s\-\(\)]{7,}\d')
DATE = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')

def parse_all(text: str) -> Dict[str, str]:
    """Pull key fields from raw document text."""
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    title = lines[0] if lines else ""
    subtitle = lines[1] if len(lines) > 1 else ""
    date = _date(text)
    desc = _desc(text)
    name, i = _name(lines)
    email = _email(lines, text)
    phone = _phone(lines, text, i)

    return {
        "title": title,
        "subtitle": subtitle,
        "date": date,
        "description": desc,
        "person_name": name,
        "email": email,
        "phone": phone,
    }

def _date(text: str) -> str:
    """First date in YYYY-MM-DD format."""
    m = DATE.search(text)
    return m.group() if m else ""

def _desc(text: str) -> str:
    """Line after 'Description:'."""
    if "Description:" in text:
        part = text.split("Description:", 1)[1]
        for l in part.splitlines():
            if l.strip():
                return l.strip()
    return ""

def _name(lines: list[str]) -> tuple[str, int]:
    """Get name from 'Name:' line."""
    for i, l in enumerate(lines):
        if l.lower().startswith("name:"):
            return l.split(":", 1)[1].strip(), i
    return "", -1

def _email(lines: list[str], text: str) -> str:
    """Prefer 'Email:' label, else fallback to regex."""
    for l in lines:
        if l.lower().startswith("email:"):
            return l.split(":", 1)[1].strip()
    m = EMAIL.search(text)
    return m.group() if m else ""

def _phone(lines: list[str], text: str, start: int) -> str:
    """Prefer 'Phone:' after name, else regex fallback."""
    if start >= 0:
        for l in lines[start + 1:]:
            if l.lower().startswith("phone:"):
                return l.split(":", 1)[1].strip()
    m = PHONE.search(text)
    return m.group() if m else ""
