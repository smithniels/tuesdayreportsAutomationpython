'''
This file will open & run SQL reports copying the outputs.
Login into a gmail account and open blank Google spreadsheets.
Format the google spread sheets (freeszing the top row, setting the title, and locking privacy settings)
Paste the copied data

TODO: The functions being called here need to be broken down and rearranged to expedite the run time
TODO: The program needs to be scheduled using the chrontabs module

Notes:
    There are SEVEN VARAIBALES fields that need to be assigned below before this is run.
    This file currently uses pyautogui to work with Sheets. The gspread module would work better, but I'm still learning
    how to use API's, so for the time being pyautogui works.
    The final step here is to send out these reports, but until I get everything where I need it to be I'm holding back from
        including that code, so I don't inundate folks with accidental emails.
    Because it's using pyautogui to count pixels, varying monitor sizes means that this code will need to be adjusted to work for some people
        I've put in python code for find the x,y coordinates of the mouse in this repo. [whereMouse.py]


'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ctypes
import subprocess
import pyautogui

#SEVEN VARIABLES
gmail  = ''            #password to gmail account
email2 = ''            #email address of gmail account
sqlpw  = ''            #password to SQL server
sql2   = '0.0.0.0'     #
sql3   = ''            #login for SQL server
script = 'C:\\'        # path to SQL file to be run
path = r''             #path to sql.exe file


def googleFormat():

        # x, y = pyautogui.position()
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # print(positionStr, end='')
        # print('\b' * len(positionStr), end='', flush=True)
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
browser = webdriver.Chrome(r'C:\Users\19258\Desktop\chromedriver.exe')
browser.get('https://docs.google.com/spreadsheets/u/0/')
action = webdriver.ActionChains(browser)

emailElem = browser.find_element_by_name("identifier")
emailElem.send_keys('email2')
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
