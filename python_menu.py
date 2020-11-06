
import os 
import subprocess as sp

def mainmenu():
    os.system('espeak-ng WelcomeToPythonMenu')
    while True:
        os.system('clear')
        os.system('tput setaf 5')
        print("""
                                                 -------------------------- 
                                                   PYTHON AUTOMATION MENU
                                                 --------------------------
              """)
        os.system('tput setaf 6')
        print("""
                                                   Press '1': Hadoop Menu
                                                   Press '2': AWS Menu
                                                   Press '3': Docker Menu
                                                   Press '4': LVM Partition Menu
                                                   Press '5': Webserver Automation
                                                   Press '0': Exit
            
              """)
        os.system('tput setaf 4')
        ch=input("\t\t\t\t\t\t      Enter Your Choice: ")
        ch = int(ch)
        if ch == 1:
            os.system("python3 hadoop.py")
        elif ch == 2:
            os.system("python3 awsautomation.py")
        elif ch == 3:
            os.system("python3 dockerautomation.py")
        elif ch == 4:
            os.system("python3 lvmautomation.py")
        elif ch == 5:
            os.system("python3 webserver.py")
        elif ch == 0:
            os.system('tput setaf 7')
            exit()
        else :
            print("Wrong Choice")

mainmenu()
