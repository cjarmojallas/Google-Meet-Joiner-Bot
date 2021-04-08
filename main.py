
import pyautogui
import time
import webbrowser
from datetime import datetime
from os import system

clock = input("Start of meeting?: ")
url = input("enter meeting url: ")
print("End of Meeting")
print("Put Minutes Please")
duration = int(input("duration of meeting:? "))

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


def autoconnect(link):
    #change the directory to your chrome directory
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new(link)

    x = 10
    time.sleep(x)
    
    #turning off camera
    pyautogui.hotkey('ctrl', 'e')

    time.sleep(2)
    
    #turning off microphonne
    pyautogui.hotkey('ctrl', 'd')

    x = 3
    time.sleep(x)
    
    #joing the meeting
    pyautogui.click(1320, 580)
    
    #will end the meeting after the given duration is done
    time.sleep(duration * 60)

    pyautogui.hotkey('alt', 'f4')

while current_time != (clock):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    system("cls")

if clock == current_time:
    autoconnect(url)







