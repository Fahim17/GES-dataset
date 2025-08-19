import pyautogui
import time
import os

folder_path = "C:\\Users\\ChinoMo\\Downloads\\Vigor"
prev_count = len(os.listdir(folder_path))

# Delay to allow time to switch to browser window
print("You have 5 seconds to place your mouse over the first image.")
time.sleep(5)

# Coordinates of the image (you can record this using pyautogui.position())
image_pos = pyautogui.position()
print(f"Captured image position: {image_pos}")

# Number of images you want to download
num_images = 2

# GSE attributes
gse_lat = pyautogui.Point(265, 802)
gse_long = pyautogui.Point(265, 760)
gse_alt = pyautogui.Point(255, 848) 
gse_pan = pyautogui.Point(260, 930)
gse_tilt = pyautogui.Point(260, 975)
img_capture = pyautogui.Point(780, 172)

# system
col_lat = pyautogui.Point(1100, 250)
col_long = pyautogui.Point(1167, 250)
col_pan = pyautogui.Point(1300, 250)
scroll = -40

moveTo_duration = 0.1
download_wait_time = 15
keypress_duration = 0.2

for i in range(num_images):
    # **********************Latitude**********************
    pyautogui.moveTo(col_lat.x, col_lat.y, duration=moveTo_duration)
    
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')


    pyautogui.hotkey('ctrl', 'c')

    pyautogui.moveTo(gse_lat.x, gse_lat.y, duration=moveTo_duration)

    pyautogui.click(button='left')
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'v')

    # **********************Longitude**********************
    pyautogui.moveTo(col_long.x, col_long.y, duration=moveTo_duration)
    
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')


    pyautogui.hotkey('ctrl', 'c')

    # pyautogui.scroll(scroll)

    pyautogui.moveTo(gse_long.x, gse_long.y, duration=moveTo_duration)

    pyautogui.click(button='left')
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'v')

    # **********************Altitude**********************
    # pyautogui.moveTo(gse_alt.x, gse_alt.y, duration=moveTo_duration)

    # pyautogui.click(button='left')

    # pyautogui.typewrite(['2', '0', '0', 'enter'], interval=0.5)

    pyautogui.moveTo(col_pan.x, col_pan.y, duration=moveTo_duration)
    
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')


    pyautogui.hotkey('ctrl', 'c')

    time.sleep(0.5)
    pyautogui.scroll(scroll)

    pyautogui.moveTo(gse_alt.x, gse_alt.y, duration=moveTo_duration)

    pyautogui.click(button='left')
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'v')

    # **********************Exp**********************
    # pyautogui.moveTo(540, 400, duration=moveTo_duration)
    # pyautogui.scroll(1)
    
    # **********************Pan**********************
    pyautogui.moveTo(gse_pan.x, gse_pan.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    pyautogui.typewrite(['1','2','0', 'enter'], interval=keypress_duration)

    # **********************Tilt**********************
    pyautogui.moveTo(gse_tilt.x, gse_tilt.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    pyautogui.typewrite(['7', '0', 'enter'], interval=keypress_duration)




    # Download
    pyautogui.moveTo(img_capture.x, img_capture.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    # time.sleep(download_wait_time)
    while True:
        time.sleep(1)  # Check every 1 second
        current_count = len(os.listdir(folder_path))
        if current_count != prev_count:
            print(f"Change detected! Previous: {prev_count}, Now: {current_count}")
            prev_count = current_count
            break
