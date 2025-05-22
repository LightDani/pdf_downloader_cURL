import os
import re
import subprocess
from PIL import Image
import pytesseract
from pypdf import PdfWriter

# Set the path to the Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


def run_ocr_and_create_searchable_pdf(images, output_pdf_path):
    """
    Generate a searchable PDF by applying OCR to each image and embedding invisible text.
    Each image is converted to a single-page PDF with OCR text, then merged into a final PDF.
    """
    partial_pdfs = []

    for i, img in enumerate(images):
        # Convert image to OCR'd PDF with invisible text layer
        pdf_bytes = pytesseract.image_to_pdf_or_hocr(img, extension="pdf")

        # Save temporary single-page PDF
        temp_pdf_path = f"tmp/page_{i}.pdf"
        with open(temp_pdf_path, "wb") as f:
            f.write(pdf_bytes)

        partial_pdfs.append(temp_pdf_path)

    # Merge all individual PDFs into one multi-page searchable PDF
    merger = PdfWriter()
    for pdf in partial_pdfs:
        merger.append(pdf)
    merger.write(output_pdf_path)
    merger.close()

    # Clean up temporary page PDFs
    for pdf in partial_pdfs:
        os.remove(pdf)


def main():
    # Ensure tmp and output directories exist
    os.makedirs("tmp", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    # Read the base command from a text file and clean it up by removing extra whitespace
    with open("url.txt", "r", encoding="utf-8") as f:
        command = " ".join(f.read().split())

    # Collect user input for PDF output name, total pages, image quality, and OCR option
    name = input("Enter name of pdf: ").strip()
    pages = int(input("Enter pages: "))
    quality = int(input("Enter quality (800, 1600, 3200): "))
    searchable = (
        input("Do you want the PDF to be searchable? (y/n): ").strip().lower() == "y"
    )

    # Replace placeholders in the command string with actual values
    command = re.sub(
        r"page=\d+", "page={}", command, count=1
    )  # Placeholder for page number
    command = re.sub(
        r"w=\d+", f"w={quality}", command, count=1
    )  # Set image width based on user input
    command += (
        " -o tmp/{}.png"  # Append output filename format (e.g., 0.png, 1.png, etc.)
    )

    # Generate PNG images for each page
    images = []
    for page in range(pages):
        formatted_command = command.format(page, page)
        subprocess.run(
            formatted_command, shell=True, check=True
        )  # Run the external download/render command
        with Image.open(f"tmp/{page}.png") as img:
            images.append(img.convert("RGB"))  # Convert to RGB for consistency

    # Create final output PDF (searchable or non-searchable based on user choice)
    output_pdf_path = f"output/{name}.pdf"
    if searchable:
        run_ocr_and_create_searchable_pdf(images, output_pdf_path)
    else:
        images[0].save(
            output_pdf_path, save_all=True, append_images=images[1:]
        )  # Standard image-based PDF

    # Clean up temporary PNG files
    for i in range(pages):
        os.remove(f"tmp/{i}.png")

    print(f"PDF saved to {output_pdf_path}")


if __name__ == "__main__":
    main()
