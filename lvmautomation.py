
#!/usr/bin/python3

import subprocess as sp
import os

def avaldisk():
    os.system('tput setaf 6')
    os.system('fdisk -l | less')
    os.system('tput setaf 7')

def avalpv():
    os.system('tput setaf 6')
    os.system('pvdisplay | less')
    os.system('tput setaf 7')

def avalvg():
    os.system('tput setaf 6')
    os.system('vgdisplay | less')
    os.system('tput setaf 7')

def avallv():
    os.system('tput setaf 6')
    os.system('lvdisplay | less')
    os.system('tput setaf 7')


def pv():
    os.system('clear')
    os.system('tput setaf 1')
    print()
    print("\t\t\t\tPHYSICAL VOLUME CREATION ")
    print("\t\t\t\t-------------------------")
    print()
    os.system('tput setaf 3')
    name=input("\t\t\t\tEnter the hard disk name : ")
    os.system('tput setaf 6')
    x=sp.getstatusoutput('pvcreate {}'.format(name))
    if x[0]==0:
        print('\t\t\t\tPHYSICAL VOLUME CREATED')
        y=sp.getstatusoutput('pvdisplay {}'.format(name))
        print(y[1])
    else :
        print("PROCESS FAIL")
    os.system('tput setaf 4')
    z=input("Press Enter to Continue")
    os.system('tput setaf 7')

def vg():
    os.system('clear')
    os.system('tput setaf 1')
    print()
    print("\t\t\t\tVOLUME GROUP CREATION ")
    print("\t\t\t\t----------------------")
    print()
    os.system('tput setaf 3')
    name=input("\t\t\t\tEnter Volume Group name : ")
    name1=input("\t\t\t\tEnter the first Physical Volume name : ")
    name2=input("\t\t\t\tEnter the second Physical Volume name : ")
    os.system('tput setaf 6')
    x=sp.getstatusoutput('vgcreate {0} {1} {2}'.format(name,name1,name2))
    if x[0]==0:
        print('\t\t\t\tVOLUME GROUP CREATED')
        y=sp.getstatusoutput('vgdisplay {}'.format(name))
        print(y[1])
    else :
        print("PROCESS FAIL")

    os.system('tput setaf 4')
    z=input("Press Enter to Continue")
    os.system('tput setaf 7')

def lv():
    os.system('clear')
    os.system('tput setaf 1')
    print()
    print("\t\t\t\tLOGICAL VOLUME CREATION ")
    print("\t\t\t\t------------------------")
    print()
    os.system('tput setaf 3')
    pname=input("\t\t\t\tEnter Partition name : ")
    vname=input("\t\t\t\tEnter Volume Group name : ")
    lsize=input("\t\t\t\tEnter Size: ")
    os.system('tput setaf 6')
    x=sp.getstatusoutput('lvcreate --size {0}G --name {1} {2}'.format(lsize,pname,vname))
    if x[0]==0:
        print('\t\t\t\tLOGICAL VOLUME CREATED')
        y=sp.getstatusoutput('lvdisplay {}'.format(pname))
        print(y[1])
    else :
        print("PROCESS FAIL")

    os.system('tput setaf 4')
    z=input("Press Enter to Continue")
    os.system('tput setaf 7')

def extend():
    print("How much size you want to increase?")
    isize=input("Enter size(in GB): ")
    z=input("Enter the Logical Volume Name: ")
    x=sp.getstatusoutput("lvextend --size +{0}G  {1}".format(isize,z))
    if x[0]==0:
        y=sp.getoutput("resize2fs  {0}".format(z))
        print("SIZE INCREASE SUCCESSFULLY BY {} GB".format(isize))
    else:
        print("INCREASE FAIL")
    os.system('tput setaf 4')
    z=input("Press Enter to Continue")
    os.system('tput setaf 7')

def menu():
    while True:
         os.system('clear')
         os.system('tput setaf 5')
         print()
         print("""
                                                 LVM PARTITION AUTOMATION  
                                                 ------------------------
               """)
         print()
         os.system('tput setaf 6')
         print("""
                                               Press '1':List all Attached Disk
                                               Press '2':List all Physical Volume
                                               Press '3':List all Volume Group
                                               Press '4':List all Logical Volume
                                               Press '5':Create Physical Volume
                                               Press '6':Create Volume Group
                                               Press '7':Create Logical Volume
                                               Press '8':Extend volume
                                               Press '0':Exit
             """)
         print()
         os.system('tput setaf 3')
         ch=input("\t\t\t\t\t\t    Enter your choice: ")
         if int(ch)== 1:
             avaldisk()
         elif int(ch)== 2:
             avalpv()
         elif int(ch)== 3:
             avalvg()
         elif int(ch)== 4:
             avallv()
         elif int(ch)== 5:
             pv()
         elif int(ch)== 6:
             vg()
         elif int(ch)== 7:
             lv()
         elif int(ch)== 8:
             extend()
         elif int(ch)== 0:
             os.system('clear')
             os.system('tput setaf 7')
             exit()
         else:
             os.system('tput setaf 7')
             print("WRONG COMMAND !!!")
menu()
