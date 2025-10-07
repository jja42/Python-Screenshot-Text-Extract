import pyautogui
import keyboard
import time
import sys
import os

#The region to capture (x,y)
top_left = (450,250)
bottom_right = (1200,650)
region = (top_left[0], top_left[1], bottom_right[0]-top_left[0], bottom_right[1]-top_left[1])  

#Set Directory where Images will be Saved
screenshot_dir = "screenshots"
#Creates it if it doesn't exist
os.makedirs(screenshot_dir, exist_ok=True)

def capture_screen(region):
	timestamp = time.strftime("%Y%m%d-%H%M%S")
	filepath = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
	screenshot = pyautogui.screenshot(region=region)
	screenshot.save(filepath)
	print(f"Screenshot saved at {filepath}")
	
def set_region():
	global region, top_left, bottom_right
	region = (top_left[0], top_left[1], bottom_right[0]-top_left[0], bottom_right[1]-top_left[1]) 

def main():
	global top_left, bottom_right
	print("Place your mouse at the Top Left of the area you want to capture.\n Then Press '1' to Set Top Left of Capture\n")
	print("Place your mouse at the Borrom Right of the area you want to capture.\n Then Press '2' to Set Bottom Right of Capture\n")
	print("Press 'Z' to start capturing screenshots...")
	print("Press 'Esc' to quit the program.")
    
	while True:
		#Use this to help with setting Region
		if keyboard.is_pressed('1'):
			print("Top Left of Selection Set to")
			print(pyautogui.position())
			top_left = pyautogui.position()
			set_region()
			time.sleep(1)
		if keyboard.is_pressed('2'):
			print("Bottom Right of Selection Set to")
			print(pyautogui.position())
			bottom_right = pyautogui.position()
			set_region()
			time.sleep(1)
		if keyboard.is_pressed('Z'):
			print("Capturing screenshot...")
			capture_screen(region)
			time.sleep(1)  #1 second delay to prevent duplicate captures

		if keyboard.is_pressed('Esc'):
			print("Exiting program...")
			sys.exit()  #Quit Out

		time.sleep(0.1)  #Additional delay to prevent high CPU usage

main()
