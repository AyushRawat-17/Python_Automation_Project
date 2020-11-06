
#!/usr/bin/python3

import os
import subprocess as sp

def launchcont():
    os.system('clear')
    os.system('tput setaf 5')
    print("""
                                        Launch Container
                                       ------------------
    
          """)
    os.system('tput setaf 6')
    name=input("\t\t\t\t   Enter Container name: ")
    os.system('tput setaf 3')
    print("\t\t\t\t   Select From Follwing Image")
    print() 
    os.system('docker images')
    print()
    os.system('tput setaf 6')
    image=input("\t\t\t\t   Enter Image name: ")
    output=sp.getstatusoutput("docker run -itd --name {0} {1}".format(name,image))
    if output[0]==0:
        os.system('tput setaf 2')
        print("\t\t\t\t   {} Container Launched".format(name))
    else :
        os.system('tput setaf 1')
        print("\t\t\t\t   Container Launch Fail")
    s=input("PRESS ENTER TO CONTINUE")

def stopcont():
    os.system('clear')
    print()
    os.system('tput setaf 5')
    print("""                              
                                            Stop Container
                                            --------------
         
          """)
    os.system('tput setaf 6')
    name=input("\t\t\t\t   Enter  Container name: ")
    output=sp.getstatusoutput("docker stop {}".format(name))
    if output[0]==0:
        os.system('tput setaf 2')
        print("\t\t\t\t   {} Container Stopped Successfully ".format(name))
    else :
        os.system('tput setaf 1')
        print("\t\t\t\t   Process Failled")
    s=input("PRESS ENTER TO CONTINUE")

def pullimage():
    os.system('clear')
    os.system('tput setaf 5')
    print("""
   
                                            Pull Image
                                            ----------

         """)
    os.system('tput setaf 6')
    osname=input("\t\t\t\t   Enter Image name: ")
    output=sp.getstatusoutput('docker pull {0}'.format(osname))
    if output[0]==0:
        os.system('tput setaf 2')
        print("\t\t\t\t   {} Image Pulled Successfully ".format(osname))
    else :
        os.system('tput setaf 1')
        print("\t\t\t\t   Process Failled")
    s=input("PRESS ENTER TO CONTINUE")

def checkruncont():
    os.system('clear')
    os.system('tput setaf 5')
    print("""
                                    
                                    Check Running Container
                                    -----------------------

        """)
    os.system('tput setaf 2')
    os.system('docker ps')
    print()
    s=input("PRESS ENTER TO CONTINUE")

def checkallcont():
    os.system('clear')
    os.system('tput setaf 5')
    print("""
            
                                       Check All Container
                                       -------------------
            
            """)
    os.system('tput setaf 2')
    os.system('docker ps -a')
    print()
    s=input("PRESS ENTER TO CONTINUE")

def checkavalimage():
    os.system('clear')
    os.system('tput setaf 5')
    print("""
                                     Check Available Image
                                     ---------------------
            
            """)
    os.system('tput setaf 2')
    os.system('docker images')
    print()
    s=input("PRESS ENTER TO CONTINUE")

def removeimage():
    os.system('clear')
    os.system('tput setaf 5')
    print("""
            
                                        Remove Images
                                       ---------------
           
         """)
    os.system('tput setaf 6')
    image=input("\t\t\t\t   Enter Image Name: ")
    output=sp.getstatusoutput('docker rmi {}'.format(image))
    if output[0]==0:
        os.system('tput setaf 2')
        print("\t\t\t\t   {} Image Removed Successfully ".format(image))
    else :
        os.system('tput setaf 1')
        print("\t\t\t\t   Process Failled")
    print()
    s=input("PRESS ENTER TO CONTINUE")

def removeallimage():
    os.system('clear')
    os.system('tput setaf 5')
    print("""
                                    Remove All Images
                                   -------------------

            """)
    output=sp.getstatusoutput('docker rmi `docker images -q`')
    if output[0]==0:
        os.system('tput setaf 2')
        print("\t\t\t\t  All Image Removed Successfully ")
    else :
        os.system('tput setaf 1')
        print("\t\t\t\t   Process Failled")

    print()
    s=input("PRESS ENTER TO CONTINUE")

def removecont():
    os.system('clear')
    os.system('tput setaf 5')
    print("""
                                            Remove Container
                                           ------------------

        """)
    os.system('tput setaf 6')
    osname=input("\t\t\t\t   Enter Container Name: ")
    output=sp.getstatusoutput('docker rm {}'.format(osname))
    if output[0]==0:
        os.system('tput setaf 2')
        print("\t\t\t\t   {} Container Removed Successfully ".format(osname))
    else :
        os.system('tput setaf 1')
        print("\t\t\t\t   Process Failled")
    print()
    s=input("PRESS ENTER TO CONTINUE")

def removeallcont():
    os.system('clear')
    os.system('tput setaf 5')
    print("""
                                     Remove all Container
                                     --------------------
            
          """)
    output=sp.getstatusoutput('docker rm `docker ps -q`')
    if output[0]==0:
        os.system('tput setaf 2')
        print("\t\t\t\t   All Containers Removed Successfully ")
    else :
        os.system('tput setaf 1')
        print("\t\t\t\t   Process Failled")
    print()
    s=input("PRESS ENTER TO CONTINUE")


def dockermenu():
    while True:
        os.system('clear')
        os.system('tput setaf 5')
        print("""
                                                        DOCKER MENU
                                                        -----------
            """)
        os.system('tput setaf 6')
        print("""                                             
                                                 Press '1':Launch Container
                                                 Press '2':Stop Running Container
                                                 Press '3':Pull Docker Images
                                                 Press '4':Check Running Container
                                                 Press '5':Check All Container
                                                 Press '6':Check Available Images
                                                 Press '7':Remove Image
                                                 Press '8':Remove all Images
                                                 Press '9':Remove a Container
                                                 Press '10':Remove all Container
                                                 Press '0':Exit
            """)
        os.system('tput setaf 4')
        ch=input("\t\t\t\t\t          Enter your Choice: ")
        ch=int(ch)
        if ch==1:
            launchcont()
        elif ch ==2:
            stopcont()
        elif ch ==3:
            pullimage()
        elif ch ==4:
            checkruncont()
        elif ch ==5:
            checkallcont()
        elif ch ==6:
            checkavalimage()
        elif ch ==7:
            removeimage()
        elif ch ==8:
            removeallimage()
        elif ch ==9:
            removecont()
        elif ch ==10:
            removeallcont()
        elif ch ==0:
            os.system('tput setaf 7')
            exit()
        else:
            print("Wrong Choice")

dockermenu()

x=input()
