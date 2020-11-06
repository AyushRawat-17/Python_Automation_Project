
import subprocess as sp
import os

def install():
    output=sp.getstatusoutput('dnf install httpd -y')
    if output[0]== 0:
        print("\t\t\t\t\t   HTTPD Installed Successfully")
    else:
        print("\t\t\t\t\t   Failed")

def configure():
    file=input("Enter File with path: ")
    os.system("cp {} /var/www/html".format(file))
    os.system("systemctl start httpd")
    print("\t\t\t\t\t   Webserver Configured")

def stop():
    os.system("systemctl stop httpd")
    print("\t\t\t\t\t   Webserver Stopped ")

def menu():
    while True:
       os.system("clear")
       os.system('tput setaf 5')
       print("""
                                                      Webserver Configuration
                                                      -----------------------
            """)
       os.system('tput setaf 6')
       print("""
                                                      Press '1': Install HTTPD
                                                      Press '2': Configure Webserver 
                                                      Press '3': Stop Webserver
                                                      Press '0': Exit
            """)
       os.system('tput setaf 4')
       ch = input("\t\t\t\t\t\t        Enter your choice: ")
       ch = int (ch)
       if ch == 1:
           install()
       elif ch == 2:
           configure()
       elif ch == 3:
           stop()
       elif ch == 0:
           os.system('tput setaf 7')
           exit()
menu()
