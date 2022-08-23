
This generation is exposed to a lot of unwanted content and kids who are underaged
visiting malicious websites has become common. It is very easy for one to go Incognito
or delete history to prevent parents from tracking their internet activity.
This Python script aims to tackle this problem preventing the user from entering
unwanted websites. The target audience for this product are parents who want their kids
to be cyber-protected.
A set of keywords is stored, one of which when typed by the user triggers a beep sound
and a warning pop-up. The current window immediately closes preventing the user from
entering the website.

PyWin32 library is used in the script from which modules win32api, win32gui, timer,
win32file and win32con have been used
Modules used:
1. win32api
● Beep function is used to set the alarm
● SetCursorPos sets the mouse cursor position to said coordinates
2. win32gui
● MessageBox function is used to trigger the warning pop-up
3. win32file
● CopyFile function is used to clear the current keylog file. An empty text file is created
and is copied onto the existing keylog file to clear it.
4. win32con
● MOUSEEVENTF_LEFTDOWN presses the left mouse button
● MOUSEEVENTF_LEFTUP releases the left mouse button
Both are used simultaneously to click the exit window button.
5. Timer
● Set_timer sets a timer and executes a function when the time elapses
● kill_timer terminates the timer function
Both are used to set a timer countdown until the window closes
