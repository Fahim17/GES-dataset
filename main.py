import pyautogui
import time

# Delay to allow time to switch to browser window
print("You have 5 seconds to place your mouse over the first image.")
time.sleep(5)

# Coordinates of the image (you can record this using pyautogui.position())
image_pos = pyautogui.position()
print(f"Captured image position: {image_pos}")

# Number of images you want to download
num_images = 1

# GSE attributes
gse_lat = pyautogui.Point(250, 802)
gse_long = pyautogui.Point(250, 760)
gse_alt = pyautogui.Point(255, 848)
gse_pan = pyautogui.Point(250, 930)
gse_tilt = pyautogui.Point(252, 975)
img_capture = pyautogui.Point(780, 172)

# system
col_lat = pyautogui.Point(1100, 250)
col_long = pyautogui.Point(1167, 250)
scroll = -40


for i in range(num_images):
    # Move to image position
    pyautogui.moveTo(gse_lat.x, gse_lat.y, duration=0.5)
    
    # Right click
    pyautogui.click(button='left')

    pyautogui.hotkey('ctrl', 'c')

    pyautogui.moveTo(col_lat.x, col_lat.y, duration=0.5)

    pyautogui.hotkey('ctrl', 'c')

    # time.sleep(1)
    
    # # Press down arrow and then Enter (or directly press 'v' if "Save image as..." is on 'v')
    # pyautogui.press('v')  # Or pyautogui.press('down', presses=2)
    # time.sleep(2)

    # # Type filename
    # pyautogui.typewrite(f'image_{i+1}.jpg')
    # time.sleep(1)

    # # Press Enter to save
    # pyautogui.press('enter')
    # time.sleep(3)

    # # Scroll down for next image or move to next
    # pyautogui.scroll(-500)
    # time.sleep(2)
