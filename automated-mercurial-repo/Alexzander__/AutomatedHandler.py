#!/usr/bin/python3.9

import os
from pathlib import Path
from time import sleep
import sys
import socket
from core.aesthetics import *
from core.datetime__ import (
    get_current_datetime,
    get_current_time,
    get_current_hour,
    get_current_minute
)
from core.logging__ import Loggerr
from core.linuxapi import linux_notification

def notification_wrapper(message):
    linux_notification(
        appname,
        message,
        mercurial_icon.absolute().as_posix()
    )

appname = "Alexzander__ repo"
mercurial_icon = Path("icons/mercurial.png")
logger_AutomatedHandler = Loggerr("AutomatedHandler")
logger_AutomatedHandler.info("script started!\n")
notification_wrapper(
    "repo handler initialized"
)   





def is_remote_server_online(ip_address):
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_client.connect((ip_address, 22))
        return True
    except socket.error as error:
        print(f"IP: {ip_address} {error}")
        return False


Alexzander__mercurial_repo_folder_path = "~/Alexzander__"
Alexzander__mercurial_repo_folder = Path(
    os.path.expanduser(Alexzander__mercurial_repo_folder_path))

#  print(Alexzander__mercurial_repo_folder)

# executed in order
commands_list = [
    # make sure you have added the keys to the keychain
    # otherwise it wont work even if you have the public key physically copied to the system
    "hg add .",
    f"hg commit -m \"{get_current_datetime()} - commit made automatically\" --addremove",
    # hg push Alexzander__ubuntu_71
    "ssh-add ~/.ssh/ubuntu_192_168_1_71",
    "hg push ssh://alexzander@192.168.1.71/mercurial_version_control/Alexzander__",
    "ssh -i ~/.ssh/ubuntu_192_168_1_71 alexzander@192.168.1.71 -t \"cd ~/mercurial_version_control/Alexzander__; hg up; echo -e \'\n\'; ls -a; echo -e \'\n$(tput bold)\033[0;32mMERCURIAL repo UPDATED successfully\033[0m\n\'\"",
    "ssh-add ~/.ssh/manjaro_192_168_1_72",
    "hg push ssh://alexzander@192.168.1.72/mercurial_version_control/Alexzander__",
    "ssh -i ~/.ssh/manjaro_192_168_1_72 alexzander@192.168.1.72 -t \"cd ~/mercurial_version_control/Alexzander__; hg up; echo -e \'\n\'; ls -a; echo -e \'\n$(tput bold)\033[0;32mMERCURIAL repo UPDATED successfully\033[0m\n\'\"",
    "",
    "",
    "",
    "",
]


ubuntu_192_168_1_71 = "192.168.1.71"
manjaro_192_168_1_72 = "192.168.1.72"


def UpdateFileSystem(prompt=True):
    ubuntu_71_online = True
    manjaro_72_online = True
    if not is_remote_server_online(ubuntu_192_168_1_71):
        ubuntu_71_online = False
    if not is_remote_server_online(manjaro_192_168_1_72):
        manjaro_72_online = False

    if ubuntu_71_online and manjaro_72_online:
        print("good. both servers are ONLINE\n")
    elif ubuntu_71_online:
        print("WARNING: only ubuntu 71 server is ONLINE")
        print("waiting 5 minutes ... to get server online")
        sleep(5 * 60)
    elif manjaro_72_online:
        print("WARNING: only manjaro 72 server is ONLINE")
        print("waiting 5 minutes ... to get server online")
        sleep(5 * 60)
    else:
        notification_wrapper("WARNING: NO server online")
        print("ERROR: NO server online. open servers NOW!")
        print("you have 10 minutes")
        sleep(10 * 60)
    print()

    if os.getcwd() != Alexzander__mercurial_repo_folder.absolute().as_posix():
        os.chdir(Alexzander__mercurial_repo_folder.absolute().as_posix())
        print(
            f"directory changed to: {Alexzander__mercurial_repo_folder_path}")
    else:
        print(f"current path is: {Alexzander__mercurial_repo_folder}")
        print(f"os.getcwd() == {os.getcwd()}")

    if prompt:
        decision = input("are you sure? [y/n]:\n>>> ")
        if decision != "y" and decision != "":
            print("aborted")
            return

    for command in commands_list:
        if command == "":
            continue

        print(f"\n{yellow_bold(command)}\n")
        os.system(command)
        print("\nsleeing 0.5 seconds ...\n")
        sleep(0.5)
    
    finish_message = f"backup finished at: {get_current_time()}\nsuccess"
    logger_AutomatedHandler.info(finish_message)
    notification_wrapper(
        finish_message
    )


def Alexzander__repo_Handler():
    while 1:
        current_hour = get_current_hour()
        current_minute = get_current_minute()
        current_time = get_current_time()
        print(f"\nCurrent Time: [ {current_time} ]\n")

        if current_hour == "15" or current_hour == "17" or current_hour == "19":
            print("\nits time for update\n")
            UpdateFileSystem(prompt=False)
            print("Alexzander__ files updated to remote servers successfully!!")
            print("sleeping for 23 hours ...")
        else:
            print("its not time for update")
            print("time for update is: [15, 17, 19]")

        print("\nsleeping 1 hour ...\n")
        sleep(60 * 10)  # 1 hour


if __name__ == "__main__":
    #  UpdateFileSystem(prompt=True)

    import sys
    args = sys.argv
    if len(args) == 2:
        if args[1] == "force":
            UpdateFileSystem()
    else:
        try:
            Alexzander__repo_Handler()
        except KeyboardInterrupt:
            print("\nprogram stopped.")
