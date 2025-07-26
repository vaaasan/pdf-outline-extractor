# Adobe Hackathon 2025 - PDF Outline Extractor (Round 1A)

## 🚀 Approach

We extract headings from a PDF using font size and layout structure.

### Key Steps:
- Extract text blocks and font size using `PyMuPDF`.
- Sort text by page and position.
- The largest font on the first page is considered the **Title**.
- Next largest fonts across the document are mapped as **H1**, **H2**, and **H3** using thresholds.

---

## 🧠 Libraries Used

- **PyMuPDF (fitz)** – for reading PDFs and extracting text and font size.
- **pdfminer.six** – backup parser in case PyMuPDF fails.
- **NumPy** – for font size clustering and heading level separation.

---

## 🛠 How to Build & Run (Locally with Docker)

### 1. Build the Docker image

```bash
docker build --platform linux/amd64 -t pdfoutline:1a .
