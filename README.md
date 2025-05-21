# pdf_downloader_cURL

A Python script for downloading and compiling PDF files from image streams, especially those loaded dynamically (such as PDFs hosted on platforms like Google Drive with no direct download permissions). This tool utilizes `cURL` commands to retrieve page images and combines them into a single PDF file.

**## Important Notice**
This tool is intended strictly for educational purposes. Do not use it to bypass copyright restrictions. Unauthorized downloading of copyrighted materials may result in legal consequences.

---

## Features
- Downloads multi-page PDFs rendered as individual images
- Supports custom quality settings (e.g., 800, 1600, 3200)
- Merges all downloaded pages into a single PDF
- Automatic cleanup of temporary image files

---

## Requirements

Install dependencies from `requirements.txt`:

`pip install -r requirements.txt`

---

## Usage

1. Prepare your cURL command:
   - Press `F12` or `Ctrl+Shift+I` to open Developer Tools.
   - Open the target PDF in your browser.
   - In DevTools, go to the `Network` tab and find a request such as `img?id=...` or `blob:https://...`.
   - Right-click it and select `Copy as cURL (cmd)` for windows user.
   - Put it into `url.txt`:
     - Ensure it contains `page=...` and `w=...`.

2. Run the script:

    `python download.py`

3. Follow the prompts:
   - Enter the output PDF filename
   - Enter the total number of pages
   - Enter the quality (options: 800, 1600, or 3200)

4. The output PDF will be saved in the `output/` folder.

---

## Example cURL snippet (cleaned)

`curl 'https://example.com/img?ck=xyz&page=0&w=1600' -H 'referer: https://...'`

---

## Output Structure
- `tmp/`: Temporary folder for storing downloaded `.png` files
- `output/`: Folder where the final `.pdf` will be saved

---

## License
Educational use only. Use responsibly.
