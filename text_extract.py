from PIL import Image
from PIL import ImageOps, ImageFilter
import cv2
import numpy as np
import pytesseract
import os

#Set Directory for Images you'd like to process
image_dir = "screenshots"

#Set Directory where Text will be Saved
text_dir = "text"
#Creates it if it doesn't exist
os.makedirs(text_dir, exist_ok=True)

#Set this if Tesseract isn't in your PATH (Windows only)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Suffix for readout files
text_file = '-readout.txt'

def preprocess_image(image):
    #Convert to grayscale
    image = image.convert('L')

    #Resize
    image = resize_image(image)

    #Auto Adjust Contrast
    image = ImageOps.autocontrast(image)
    
    #Sharpening
    image = image.filter(ImageFilter.SHARPEN)
    
    image = preprocess_with_opencv(image)
    
    return image

def preprocess_with_opencv(image):
    img = np.array(image)
    #Denoise
    img = cv2.fastNlMeansDenoising(img, h=30)
    #Adaptive Threshold
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    #Convert back to PIL Image
    img = Image.fromarray(img)
    return img
    
def resize_image(image):
	img = np.array(image)
	img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
	# Convert back to PIL Image
	img = Image.fromarray(img)
	return img

def extract_text(image_path):
    image = Image.open(image_path)
    image = preprocess_image(image)
    width, height = image.size
    text = pytesseract.image_to_string(image, lang='eng', config='--oem 3 --psm 6 -c preserve_interword_spaces=1')

    return text.strip()

def save_text_to_files(text, path):
	with open(path, 'w', encoding='utf-8') as f_t:
		f_t.write(text + '\n')

#Process all images and save to the corresponding text files
for file in sorted(os.listdir(image_dir)):
    if file.endswith(".png") or file.endswith(".jpg"):
        path = os.path.join(image_dir, file)
        text = extract_text(path)
        filename = file.removesuffix('.jpg')  
        filename = filename.removesuffix('.png')
        filePath =os.path.join(text_dir, filename + text_file)
        save_text_to_files(text, filePath)
        print(f"Text from {file} has been save.")

print("Text extraction complete. All files have been updated.")
