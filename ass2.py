import pyautogui 
import pytesseract 
from PIL import Image 

# Specify the region for screenshot width with 1000pixels and 700pixels height
x, y, width, height = 0,200,1000,700

# Region Screenshot capturing using pyautogui
def screen_capture(image_filename):
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    # Save the screenshot as png
    screenshot.save('RegionScreenshot.png')

# OCR Text Recognition using pytesseract 
def ocr_text_recognition(image_filename):
    text = pytesseract.image_to_string(Image.open(image_filename))
    return text

# Text recognition and text file generate based on Screenshot image 
def screen_scraping_ocr_generation(screenshot_input, text_output):
    screen_capture(screenshot_input)
    text = ocr_text_recognition(screenshot_input)
    with open(text_output, 'w') as file:
        file.write(text)

# Main function here 
if __name__ == "__main__":
    screen_scraping_ocr_generation("RegionScreenshot.png","Output.txt")