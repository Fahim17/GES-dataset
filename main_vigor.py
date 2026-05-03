import pyautogui
import time
import os
import pandas as pd
import shutil
from datetime import datetime

from helper_func import calcRunTime, getExpID, write2Log

# Delay to allow time to switch to browser window
print("You have 10 seconds to place your mouse over the first image.")
time.sleep(8)
expID = getExpID()

write2Log(ExpID=expID, content=f'ExpID: {expID}\n')


# folder_path = "C:\\Users\\ChinoMo\\Downloads\\Vigor"
folder_path = '/home/fahimul/Downloads/vigor_temp'
prev_count = len(os.listdir(folder_path))

dst_folder = '/home/fahimul/Downloads/Vigor'


ct_nm = 'Chicago' # Chicago NewYork SanFrancisco Seattle
df = pd.read_csv(f'csv/{ct_nm}_all_images.csv')
all_values = df.img.values.tolist()
folder_names = []
for item in all_values:
    folder_name = item.split(',')
    folder_names.append(f'{folder_name[0]}_{folder_name[1]}_{folder_name[2]}')


image_pos = pyautogui.position()
print(f"Captured image position: {image_pos}")

# Number of images you want to download
start_img_number = 1700
num_images = 300

write2Log(ExpID=expID, content=f'Number of Location: {num_images}\n')

write2Log(ExpID=expID, content=f'StartTime: {datetime.now()}\n\n')
start_time = time.time()

# GSE attributes
    # home
# gse_lat = pyautogui.Point(265, 802)
# gse_long = pyautogui.Point(265, 760)
# gse_alt = pyautogui.Point(255, 848) 
# gse_pan = pyautogui.Point(260, 930)
# gse_tilt = pyautogui.Point(260, 975)
# img_capture = pyautogui.Point(780, 172)

    # office
gse_lat = pyautogui.Point(425, 1068)
gse_long = pyautogui.Point(425, 1024)
gse_alt = pyautogui.Point(408, 1113) 
gse_pan = pyautogui.Point(420, 1196)
gse_tilt = pyautogui.Point(420, 1240)
img_capture = pyautogui.Point(1100, 166)

# system
    # home
# col_lat = pyautogui.Point(1100, 250)
# col_long = pyautogui.Point(1167, 250)
# col_alt = pyautogui.Point(1300, 250)
    # office
col_lat = pyautogui.Point(1510, 350)
col_long = pyautogui.Point(1638, 350)
col_alt = pyautogui.Point(1903, 350)
col_scroll = pyautogui.Point(2554, 1362)

scroll = -40

moveTo_duration = 0.1
download_wait_time = 15
download_wait_time_per_pan = 2
keypress_duration = 0.2


for img_n in range(start_img_number, start_img_number+num_images):
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

    pyautogui.moveTo(col_alt.x, col_alt.y, duration=moveTo_duration)
    
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')


    pyautogui.hotkey('ctrl', 'c')

    # ********************Scroll*******************
    # pyautogui.scroll(scroll)

    time.sleep(0.5)
    pyautogui.moveTo(col_scroll.x, col_scroll.y, duration=moveTo_duration)
    pyautogui.click(button='left')
    # ********************************************
    pyautogui.moveTo(gse_alt.x, gse_alt.y, duration=moveTo_duration)

    pyautogui.click(button='left')
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'v')

    # **********************Exp**********************
    # pyautogui.moveTo(540, 400, duration=moveTo_duration)
    # pyautogui.scroll(1)
    
    # **********************Tilt**********************
    pyautogui.moveTo(gse_tilt.x, gse_tilt.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    pyautogui.typewrite(['7', '0', 'enter'], interval=keypress_duration)




     # **********************Pan 0 **********************
    pyautogui.moveTo(gse_pan.x, gse_pan.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    pyautogui.typewrite(['0', 'enter'], interval=keypress_duration)

    time.sleep(download_wait_time_per_pan)  

    # **********************Download**********************

    pyautogui.moveTo(img_capture.x, img_capture.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    # download_wait_time

    while True:
        time.sleep(1)  # Check every 1 second
        current_count = len(os.listdir(folder_path))
        if current_count != prev_count:
            # print(f"Change detected! Previous: {prev_count}, Now: {current_count}")
            prev_count = current_count
            break


    time.sleep(download_wait_time_per_pan)  

    # **********************Pan 60 **********************

    pyautogui.moveTo(gse_pan.x, gse_pan.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    pyautogui.typewrite(['6', '0', 'enter'], interval=keypress_duration)

    time.sleep(download_wait_time_per_pan)  

    # **********************Download**********************
    pyautogui.moveTo(img_capture.x, img_capture.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    # download_wait_time
    while True:
        time.sleep(1)  # Check every 1 second
        current_count = len(os.listdir(folder_path))
        if current_count != prev_count:
            # print(f"Change detected! Previous: {prev_count}, Now: {current_count}")
            prev_count = current_count
            break

    time.sleep(download_wait_time_per_pan)  

    # **********************Pan 120 **********************

    pyautogui.moveTo(gse_pan.x, gse_pan.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    pyautogui.typewrite(['1', '2', '0', 'enter'], interval=keypress_duration)

    time.sleep(download_wait_time_per_pan)  

    # **********************Download**********************
    pyautogui.moveTo(img_capture.x, img_capture.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    # download_wait_time
    while True:
        time.sleep(1)  # Check every 1 second
        current_count = len(os.listdir(folder_path))
        if current_count != prev_count:
            # print(f"Change detected! Previous: {prev_count}, Now: {current_count}")
            prev_count = current_count
            break
        
    time.sleep(download_wait_time_per_pan)  

    # **********************Pan 180 **********************

    pyautogui.moveTo(gse_pan.x, gse_pan.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    pyautogui.typewrite(['1', '8', '0', 'enter'], interval=keypress_duration)

    time.sleep(download_wait_time_per_pan)  

    # **********************Download**********************
    pyautogui.moveTo(img_capture.x, img_capture.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    # download_wait_time
    while True:
        time.sleep(1)  # Check every 1 second
        current_count = len(os.listdir(folder_path))
        if current_count != prev_count:
            # print(f"Change detected! Previous: {prev_count}, Now: {current_count}")
            prev_count = current_count
            break
        
    time.sleep(download_wait_time_per_pan)  

    # **********************Pan 240 **********************

    pyautogui.moveTo(gse_pan.x, gse_pan.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    pyautogui.typewrite(['2', '4', '0', 'enter'], interval=keypress_duration)

    time.sleep(download_wait_time_per_pan)  

    # **********************Download**********************
    pyautogui.moveTo(img_capture.x, img_capture.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    # download_wait_time
    while True:
        time.sleep(1)  # Check every 1 second
        current_count = len(os.listdir(folder_path))
        if current_count != prev_count:
            # print(f"Change detected! Previous: {prev_count}, Now: {current_count}")
            prev_count = current_count
            break

    time.sleep(download_wait_time_per_pan)  

    # **********************Pan 300 **********************

    pyautogui.moveTo(gse_pan.x, gse_pan.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    pyautogui.typewrite(['3', '0', '0', 'enter'], interval=keypress_duration)

    time.sleep(download_wait_time_per_pan)  

    # **********************Download**********************
    pyautogui.moveTo(img_capture.x, img_capture.y, duration=moveTo_duration)

    pyautogui.click(button='left')

    # download_wait_time
    while True:
        time.sleep(1)  # Check every 1 second
        current_count = len(os.listdir(folder_path))
        if current_count != prev_count:
            # print(f"Change detected! Previous: {prev_count}, Now: {current_count}")
            prev_count = current_count
            break



    # **********************Rename**********************
    temp_image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    # Rename them to 1.ext, 2.ext, ..., 5.ext
    for i, filename in enumerate(temp_image_files, start=0):
        ext = os.path.splitext(filename)[1]
        new_name = f"{i*60}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        # print(f"Renamed: {filename} -> {new_name}")

    # **********************Move**********************
    each_loc_folder_path = os.path.join(dst_folder, folder_names[img_n])
    print(f'folder created: {folder_names[img_n]}')
    os.makedirs(each_loc_folder_path, exist_ok=True)

    for item in os.listdir(folder_path):
        src_path = os.path.join(folder_path, item)
        dst_path = os.path.join(each_loc_folder_path, item)
        shutil.move(src_path, dst_path)


    prev_count=len(os.listdir(folder_path))

    write2Log(ExpID=expID, content=f'Item: {img_n}, Location ID: {folder_names[img_n]}\n')

write2Log(ExpID=expID, content=f'\nEndTime: {datetime.now()}\n')
end_time = time.time()
write2Log(ExpID=expID, content=f'Runtime: {calcRunTime(stt=start_time, edt=end_time)}\n')

