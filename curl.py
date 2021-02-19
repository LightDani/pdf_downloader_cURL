"""PDF(cURL) downloader using py.
For downloading pdf with no permission to download ie. pdf in google drive.
This is for educational purpose only, copyright infringement will be subject to legal sanctions.
"""

import os
import re

from bash import bash
from PIL import Image

# Pdf name
name = input("Enter name of pdf: ")
# Number of pages
pages = int(input("Enter pages: "))
# Quality pdf
quality = int(input("Enter quality (800, 1600, 3200): "))
# cURL
curl = input("Enter cURL: ")
# Fix cURL
curl = curl.replace(re.findall("page=[0-9]", curl)[0], "page={}").replace("w=800", "w={}").replace("   ", " ").replace("--compressed", "-o {}.png")

# Downloading
for page in range(pages):
  bash(curl.format(page, quality, page))

# Merging all images into pdf
first_page = Image.open("0.png").convert('RGB')
other_pages = [Image.open("{}.png".format(i)).convert('RGB') for i in range(1, pages)]
first_page.save("{}.pdf".format(name), save_all=True, append_images=other_pages)

# Finally delete all images
for i in range(pages):
  os.remove("{}.png".format(i))
