from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ctypes
import subprocess
import pyautogui

gmail = 'Fred4000!'
sqlpw   = 'Fred123@'
sql2  = '1010.235.1.240.235.1.240nsmithFred123@'
sql3  = 'nsmith'


def googleFormat():
    
            #x, y = pyautogui.position()
            #positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            #print(positionStr, end='')
            #print('\b' * len(positionStr), end='', flush=True)
        time.sleep(3)
        pyautogui.moveTo(x = 533, y = 157)
        time.sleep(.2)
        pyautogui.click()
        time.sleep(.4)
        pyautogui.moveTo(x = 578, y = 200)
        time.sleep(.2)
        pyautogui.click()
        time.sleep(.4)
        pyautogui.typewrite('Freeze 1 row')
        time.sleep(.5)
        pyautogui.press('enter')
        time.sleep(.1)
        pyautogui.moveTo(x = 87,y = 280)
        time.sleep(.1)
        pyautogui.doubleClick()
        time.sleep(.1)
        pyautogui.keyDown('ctrl')
        time.sleep(.1)
        pyautogui.typewrite('b')
        time.sleep(.1)
        pyautogui.keyUp('ctrl')
        time.sleep(.1)
        pyautogui.typewrite('is this bold enough?')
        return print('done')


############ OPEN and RUN SQL 
script = 'C:\\Users\\nsmith\\Desktop\\Tuesday.sql' 

path = r'C:\Program Files (x86)\Microsoft SQL Server\140\Tools\Binn\ManagementStudio\Ssms.exe'

subprocess.Popen("%s %s" % (path, script))

time.sleep(10)

i = 0
while i < 3:    
    pyautogui.press('tab')
    i += 1
time.sleep(1)
pyautogui.typewrite(sqlpw)
pyautogui.press('enter')
time.sleep(1)

pyautogui.press('f5')

#10.235.1.240    
############ OPEN and RUN ChromePress Ctrl-C to quit.

browser = webdriver.Chrome()
browser.get('https://docs.google.com/spreadsheets/u/0/')
action = webdriver.ActionChains(browser)

emailElem = browser.find_element_by_name("identifier")
emailElem.send_keys('nsmith@breadforthecity.org')
emailElem.send_keys(Keys.RETURN)

time.sleep(1)
emailElem1 = browser.find_element_by_name("password")
emailElem1.send_keys(gmail)
emailElem1.send_keys(Keys.RETURN)

time.sleep(1)

### TO-DO - Go to SQL Copy data 

### TO-DO - Share sheets with people

browser.get('https://docs.google.com/spreadsheets/create')
browser.maximize_window()
googleFormat()


