import argparse
import json
from parser.extract_features import extract_layout_by_page
from parser.extract_headings import extract_headings

def main(pdf_path):
    layout_by_page = extract_layout_by_page(pdf_path)
    headings = extract_headings(layout_by_page)

    output = {
        "title": pdf_path.split("/")[-1].replace(".pdf", ""),
        "outline": headings
    }

    output_path = pdf_path.replace(".pdf", "_outline.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ JSON saved to: {output_path}")
    print("\nDetected Headings:")
    for h in headings:
        print(f"{h['level']} | Page {h['page'] + 1}: {h['text']}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf', type=str, required=True)
    args = parser.parse_args()
    main(args.pdf)
