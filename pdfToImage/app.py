import tkinter as tk
import cv2
import pdf2image
from PIL import Image
from tkinter import filedialog


root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

#constants
PDF_PATH = file_path
DPI = 150
OUTPUT_FOLDER = None
FIRST_PAGE = None
LAST_PAGE = None
FORMAT = 'jpg'
THREAD_COUNT = 1
USERPWD = None
USE_CROPBOX = False
STRICT = False

pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
#image_to_segment = cv2.imread(file_path)
#segmenter(image_to_segment)

count = 1
for image in pil_images:
    #cv2.imwrite('page_'+ str(save), image)
    image = image.save("page"+str(count)+".jpg")
    count = count+1
