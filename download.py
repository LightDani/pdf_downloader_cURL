import os
import re
import subprocess
from PIL import Image


def main():
    # Ensure tmp and output directories exist
    os.makedirs("tmp", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    # Read the base command from a text file and clean it up by removing extra whitespace
    with open("url.txt", "r", encoding="utf-8") as f:
        command = " ".join(f.read().split())

    # Collect user input for PDF output name, total pages, and image quality
    name = input(
        "Enter name of pdf: "
    ).strip()  # Strip to remove any accidental whitespace
    pages = int(input("Enter pages: "))
    quality = int(input("Enter quality (800, 1600, 3200): "))

    # Replace the dynamic parts of the command with format placeholders
    # This makes it easy to substitute actual values in the loop below
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
    for page in range(pages):
        formatted_command = command.format(
            page, page
        )  # Inject page number in placeholders
        subprocess.run(formatted_command, shell=True, check=True)  # Run the command

    # Merge all generated images into a single PDF
    images = []
    for i in range(pages):
        # Open each PNG and convert to RGB (necessary for saving to PDF)
        with Image.open(f"tmp/{i}.png") as img:
            images.append(img.convert("RGB"))

    # Save the first image and append the rest to create the PDF
    output_pdf_path = f"output/{name}.pdf"
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])

    # Clean up temporary PNG files after creating the PDF
    for i in range(pages):
        os.remove(f"tmp/{i}.png")

    print(f"PDF saved to {output_pdf_path}")


if __name__ == "__main__":
    main()  # Entry point of the script
