import argparse
import json
import csv
import sys
from pathlib import Path

from parser.uploader import validate
from parser.extractor import extract_text
from parser.info_parser import parse_all

def process_file(path: Path, out_json: Path | None = None, to_csv: bool = False) -> dict:
    """Run full pipeline: validate → extract → parse → save JSON/CSV.

    Args:
        path: Path to the input file.
        out_json: Optional path to save JSON output.
        to_csv: If True, also write CSV output.

    Returns:
        Parsed information as a dictionary.
    """
    path = validate(path)
    text = extract_text(path)
    data = parse_all(text)

    json_path = out_json or path.with_suffix(".json")
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    if to_csv:
        csv_path = json_path.with_suffix(".csv")
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(data.keys())
            writer.writerow(data.values())

    return data

def main() -> None:
    """CLI entry point for the document parser."""
    parser = argparse.ArgumentParser(description="Extract structured info from PDF/DOCX files")
    parser.add_argument("input", type=Path, help="Path to the input file")
    parser.add_argument("-o", "--output", type=Path, help="Output JSON path")
    parser.add_argument("--csv", action="store_true", help="Also export to CSV")

    args = parser.parse_args()

    try:
        result = process_file(args.input, args.output, args.csv)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"JSON saved to: {args.output or args.input.with_suffix('.json')}")
    if args.csv:
        print(f"CSV saved to: {(args.output or args.input.with_suffix('.json')).with_suffix('.csv')}")

if __name__ == "__main__":
    main()
