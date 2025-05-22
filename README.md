# pdf_downloader_cURL

A Python script for downloading and compiling PDF files from image streams, especially those loaded dynamically (such as PDFs hosted on platforms like Google Drive with no direct download permissions). This tool utilizes `cURL` commands to retrieve page images and combines them into a single PDF file.

**## Important Notice**
This tool is intended strictly for educational purposes. Do not use it to bypass copyright restrictions. Unauthorized downloading of copyrighted materials may result in legal consequences.

---

## Features
- Downloads multi-page PDFs rendered as individual images
- Supports custom quality settings (e.g., 800, 1600, 3200)
- Option to create **searchable PDFs** with invisible OCR text
- Merges all downloaded pages into a single PDF
- Automatic cleanup of temporary image and intermediate files

---

## Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Make sure **Tesseract OCR** is installed on your system:
- **Ubuntu/Debian**: `sudo apt install tesseract-ocr`
- **macOS (Homebrew)**: `brew install tesseract`
- **Windows**: Download from GitHub: https://github.com/tesseract-ocr/tesseract/wiki 

---

## Usage

1. **Prepare your cURL command**:
- Press `F12` or `Ctrl+Shift+I` to open Developer Tools.
- Open the target PDF in your browser.
- In DevTools, go to the `Network` tab and find a request such as `img?id=...` or `blob:https://...`.
- Right-click it and select `Copy as cURL (cmd)` (for Windows).
- Save it in `url.txt`:
  - Ensure it contains `page=...` and `w=...`.

2. **Run the script**:

   ```
   python download.py
   ```

3. **Follow the prompts**:
   - Enter the output PDF filename
   - Enter the total number of pages
   - Enter the quality (options: 800, 1600, or 3200)
   - Choose whether to generate a **searchable PDF** (y/n)

4. The output PDF will be saved in the `output/` folder.

---

## Example cURL snippet (cleaned)

``` 
curl 'https://example.com/img?ck=xyz&page=0&w=1600' -H 'referer: https://...'
```

---

## Output Structure
- `tmp/`: Temporary folder for storing downloaded `.png` and `.pdf` chunks
- `output/`: Folder where the final `.pdf` is saved

---

## Notes on Searchable PDF
- If enabled, the script uses Tesseract OCR to extract text from each image.
- The output PDF will contain invisible text over the original image, making it fully **searchable and selectable**.
- This works best with clean, high-resolution images (e.g., 1600 or 3200 quality).

---

## License
Educational use only. Use responsibly.
