#!/usr/bin/env python3
import subprocess, os, sys
from time import sleep
from selenium import webdriver


# WEB DRIVER INIT / GO-TO ARCH WEBSITE
driver = webdriver.Chrome()
driver.get("https://archlinux.org/download")


# FIND AND CLICK TORRENT DOWNLOAD LINK
link = driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul[2]/li[2]/a')
link.click()
sleep(3)
driver.close()


# GET USER AND PATH INFO / CHDIR INTO DOWNLOADS FOLDER
usr = subprocess.getoutput("echo $USER")
path = str(os.getcwd())
os.chdir(f'/home/{usr}/downloads')


# ITERATE OVER FOLDER TO FIND TORRENT FILE
dir_contents = os.listdir()
for x in dir_contents:
    if "archlinux" in x:
        print(x)
        arch_torrent = x


# SEND TORRENT TO TRANSMISSION-CLI TO DOWNLOAD
# KILL TRANSMISSION WHEN FINISHED
subprocess.call(f'transmission-cli -f "{path}/kill_transmission.sh" {arch_torrent}', shell=True)
os.system('clear')
print('LATEST ARCH ISO HAS BEEN DOWNLOADED')


# CLEAN UP TRANSMISSION CACHE
try:
    dir_contents = os.listdir()
    for x in dir_contents:
        if ".torrent" in x:
            subprocess.call(f'rm {x}', shell=True)
    
    os.system(f'cd /home/{usr}/.config/transmission/torrents && sudo rm *')
    os.system(f'cd /home/{usr}/.config/transmission/resume && sudo rm *')
except:
    print("no files to clean up... moving on...")


# FIND DOWNLOADED ISO
for x in os.listdir():
    if "arch" in x:
        iso_file = str(x)

# RENAME ISO TO 'archlinux.iso'
os.system(f'mv {iso_file} archlinux.iso')
iso_file = 'archlinux.iso'


# BURN ISO TO DISK (FLASH DRIVE)
print(f"Ready to burn ISO image '{iso_file}' to disk...\n")
print("AVAILABLE DISKS")
list_dev = subprocess.getoutput('lsblk')
print(list_dev)
print("\n")
print("Enter device to burn ISO image to.")
print("If the device is not connected, please connect it and enter is path.")

dev_input = input("> ")
if dev_input == 'q':
    print("Program Terminated."); sleep(1)
    os.system('clear')
    quit()
else:
    dd_cmd = f'sudo dd if=/home/{usr}/downloads/{iso_file} of={dev_input} bs=4M status=progress; sync'
    os.system(dd_cmd)


# CLEAR SCREEN AND PRINT SUCCESS MSG
os.system('clear')
print(f'{iso_file} has been written to {dev_input}\n')


