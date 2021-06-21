import cv2
import tkinter as tk
import time
import numpy as np
import keyboard




#Function to make the alert window
def WindowPopUp(Title = "New Window",Size_X = 750, Size_Y = 500):
    #Creates window object
    Win = tk.Tk()
    #Set window
    Win.title(Title)
    
    #Win.configure(width=Size_X, height=Size_Y)
    #Win.configure(bg='purple')
    text = tk.Text(Win,width=Size_X, height=Size_Y)
    text.pack()

    text.insert('100.0', 'Human Detected, prepare to be eliminated')
    
    
    return Win

#Renturn a bool if their is motion by compaire two frames
def IsMotion(vid):
    #Gets frist frame
    ret, frame01 = vid.read()
    #Waits for 1 second
    time.sleep(1)
    #Gets second frame
    ret, frame02 = vid.read()
    diff = cv2.subtract(frame01,frame02)
    #cv2.imshow('test', diff)
    arr = np.uint8(diff)
    ar = arr.sum()
    
    '''A little text code block
    cv2.imshow("Frame 01", frame01)
    cv2.imshow("Frame 02", frame02)
    cv2.imshow("Diff", diff)
    print(ar)'''
    
    if (ar < 5000000):
        return False
    return True

    
    

# define a video capture object
vid = cv2.VideoCapture(0)








while(True):

    while(True):
          
          check = IsMotion(vid)
          #print(check)
          if (check):
              break


          if keyboard.is_pressed("p"):
              break

            
    if keyboard.is_pressed("p"):
        break
    
    win = WindowPopUp("Death", 1000,1000)
    win.update()
    time.sleep(5)
    win.destroy()
    

  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


