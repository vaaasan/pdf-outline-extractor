import os
import json
from utils import extract_title_and_headings

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            out_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))

            result = extract_title_and_headings(pdf_path)

            with open(out_path, "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
