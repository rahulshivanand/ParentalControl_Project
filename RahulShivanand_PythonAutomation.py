"""PseudoCode:
1. Initialise array with the keywords. Create a separate empty file named key_log.txt manually.
2. Define mouse click function which closes the window
3. Define Keyboard function
4. Function writes characters into a file and listener is set up which joins each thread to main thread
5. Performs the following if space,enter or tab is pressed
6. Checks if the text file contains the initialised keywords
7. If keyword found, sets off an annoying beep sound and a warning message.
8. Immediately closes the window
9. Clears the keylog file for fresh keylog inputs

"""

from pynput.keyboard import Listener, Key
from win32gui import *
from win32api import *
import win32con
from win32file import *
from timer import *

filename = "keylog.txt"  # The file to write characters to 
f1 = "key_log.txt"
ar = ["unwanted","websites"] #array of keywords which shouldn't be typed

def click():  #function which closes the window 
    SetCursorPos((10000,0))
    mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 10000, 0, 0, 0)
    mouse_event(win32con.MOUSEEVENTF_LEFTUP, 10000, 0, 0, 0)


def on_press(key):  
    f = open(filename, 'a')  # Open the file 

    if hasattr(key, 'char'):  # Write the character pressed if available
        f.write(key.char)       
    elif key == Key.space or key == Key.enter or key == Key.tab:
        f.close()   
        f= open(filename,'r')       #close and reopen file in read mode
        readfile= f.read()      
        for line in ar:      #if our keyword is typed perform following 
            if line in readfile:  
                Beep(1000,5000)        #alert sound 
                MessageBox(0,"Keyword detected","Warning",4096)    #alert message    
                CopyFile(f1,filename,0)    #clears the current keylof file
                i= set_timer(10,click()) #timer set after which mouse click is executed
                kill_timer(i)
            
            
        CopyFile(f1,filename,0)    #clears the current keylof file
              
                 
    f.close()  # Close the file 
with Listener(on_press=on_press) as listener:  # Setup the listener
    listener.join()  # Join the thread to the main thread 
         