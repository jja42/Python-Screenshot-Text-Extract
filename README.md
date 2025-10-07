# Python Screenshot & Text Extractor

Two simple Python scripts that allow you to capture screenshots and extract text.

## Overview

### **Screenshot Tool** (`screenshot.py`)
Captures a **Customizable Region** of your screen instantly with a single key press.  
Unlike most screenshot tools, you only need to set the capture region **once**. Then you can take as many screenshots as you want without reselecting.

### **Text Extraction Tool** (`extract_text.py`)
Extracts text from your screenshots using **OCR (Optical Character Recognition)** via [Tesseract](https://github.com/tesseract-ocr/tesseract).  
This is best suited for screenshots that are all or mostly text. It handles **batch processing**, meaning that you don't need to extract one by one.

### Why?
If you want to take multiple images of a set region without having to click and drag the screenshot area over and over again, this is for you.
If you want to get text from a screenshot of a video or a game, or text from a site that won't let you Ctrl +C, this is for you.

---

## How To Use

### Screenshot Tool
- Run: python screenshot.py
- Use the Following Key Presses:
  - `1` → Set top-left corner  
  - `2` → Set bottom-right corner  
  - `Z` → Capture screenshot  
  - `Esc` → Quit program  
- Automatically saves images with timestamps in a `screenshots/` folder  (can be changed)

### Text Extraction Tool
- Run: python extract_text.py
- Extracts text from all images in a folder  
- Uses preprocessing:
  - Grayscale conversion  
  - Auto contrast  
  - Denoising and sharpening  
  - Adaptive thresholding  
  - Upscaling for better OCR accuracy  
- Saves each image’s extracted text as a separate `.txt` file in a `text/` folder (can be changed)

---

## 🧩 Requirements

- **Python 3.8+**
- **Dependencies:**
  ```bash
  pip install pyautogui keyboard pillow pytesseract opencv-python numpy

    Tesseract OCR:

        🪟 Windows: Download installer

        🍎 macOS: brew install tesseract

        🐧 Linux (Debian/Ubuntu): sudo apt install tesseract-ocr

If you’re on Windows, update this line in extract_text.py if Tesseract isn’t in your PATH:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    Extract text from unselectable UIs or copy-protected websites

    Batch transcribe multiple text-only screenshots

    Build your own automated OCR workflow
