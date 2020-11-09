
import subprocess as sp
import os

def install():
    os.system('dnf install httpd -y')
    print("\t\t\t\t\t   HTTPD Installed Successfully")

def configure():
    file=input("Enter File with path: ")
    os.system("cp {} /var/www/html".format(file))
    os.system("systemctl start httpd")
    print("\t\t\t\t\t   Webserver Configured\n\n")
    print("Now, Open Web Browser and type ip-address.....")

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
                                                      Press '1': Install Webserver
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
