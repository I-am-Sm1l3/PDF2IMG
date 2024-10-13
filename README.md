
## PDF to Image Extractor:
The funny thing is that i tried compiling this script and GUESS!!! how the compiled file look like?Well! It took 63MB space😂.

## Overview

This is a simple Python script that extracts each page of a PDF document and saves it as an individual PNG image. It uses the **PyMuPDF** library (imported as `fitz`) for handling PDF files.

## Features

- **Extract Pages**: Convert all pages of a PDF to PNG images.
- **Easy to Use**: Just specify the PDF file and run the script.
- **Organized Output**: All images are saved in a dedicated folder.

## Requirements

- PyMuPDF (`fitz`)

You can install PyMuPDF using pip:

```bash
pip install PyMuPDF
```
## Usage:
```bash
python PDF2IMG.py -f your-file.pdf
```
## Why I Created This?
I wanted to extract images from a PDF 📄 but found that most online tools were either filled with ads 📢, had limited features ⚙️, or required too many permissions 🔒. To avoid these hassles and take control 💪, I decided to create a simple Python script 🐍 to extract full pages as images 🖼️. There's so much more to add, like a function to extract only the desired page or pages, but I'll do it later ⏳.


