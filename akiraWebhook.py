##################################################################################################################
#           __   .__              __      __      ___.   .__                   __                               #
#   _____  |  | _|__|___________ /  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __                            #
#   \__  \ |  |/ /  \_  __ \__  \\   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ /                            #
#    / __ \|    <|  ||  | \// __ \\        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <                             #
#   (____  /__|_ \__||__|  (____  /\__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \                            #
#        \/     \/              \/      \/       \/    \/     \/                   \/                            #
#                                                                                                                #
#                                                                                made by akira   04/05/2020      #
#                                                                               https://github.com/akira-trinity #
##################################################################################################################




import time
import requests
import os


def clear():
    if os.name == 'nt':
        os.system("cls")
        os.system("color 2") 
    else:
        os.system("clear")

clear()

def term():
    if os.name == 'nt':
        os.system("color 2")
        print("\
\n\
            __   .__              __      __      ___.   .__                   __    \n\
    _____  |  | _|__|___________ /  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __ \n\
    \__  \ |  |/ /  \_  __ \__  \\   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ /  \n\
     / __ \|    <|  ||  | \// __ \\        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <  \n\
    (____  /__|_ \__||__|  (____  /\__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \ \n\
         \/     \/              \/      \/       \/    \/     \/                   \/ ")


        print("\
\n\
\n\
\n\
            [0] Spam \n\
            [1] Clear \n\
            [2] Exit \n\
\n\
")
    else:
        print("\033[31m\
\n\
            __   .__              __      __      ___.   .__                   __    \n\
    _____  |  | _|__|___________ /  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __ \n\
    \__  \ |  |/ /  \_  __ \__  \\   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ /  \n\
     / __ \|    <|  ||  | \// __ \\        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <  \n\
    (____  /__|_ \__||__|  (____  /\__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \ \n\
         \/     \/              \/      \/       \/    \/     \/                   \/ \n\
\n\
                                                                               made by akira   04/05/2020 \n\
                                                                               https://github.com/akira-trinity \n\
\n\
\n\
\033[0m")


        print("\033[34m\
\n\
\n\
\n\
            [0] Spam \n\
            [1] Clear \n\
            [2] Exit \n\
\n\
\033[0m")
        
term()



terminal = True
choice=0

while terminal:
    if os.name == 'nt':
        os.system("color 2")
        choice=input("\n           akiraWebhook [>] ")
    else:
        choice=input("\033[35m\n           akiraWebhook [>] \033[0m")

    
    if choice == "0":
        if os.name == 'nt':
            os.system("color 4d")
            contenu = input("\n           [+]Input the content of the message.[Want to load the content of a .txt file? Put txt] [>] ")
            if contenu == 'txt':
                path = input("\n           [+]Input the path to the .txt file.[>] ")
                os.chdir(path)
                file_ipt = input("\n           [+]Input the name to the .txt file.(Without the extension!)  [>] ")
                file = (file_ipt + ".txt")
                file_content=open(file, "r")
                contenu = file_content.read()
                file_content.close()
            webhook = input("\n           [+]Input the URL of the webhook. [>] ")
            spam = input("\n           [+]Input the amount of messages that is going to be send. [>] ")
            tts_statut = input("\n           [+]Do you want to make TTS enabled? [Y/N]. [>] ")
            if tts_statut == "Y":
                tts = "true"
            elif tts_statut == "N":
                tts = "false"
            payload = {
                "content": contenu,
                "tts": tts,
            }
            ctn = 0
            print("\n\n           [+]The spam has started. \n")
            while ctn<spam:
                ctn+=1
                requests.post(webhook, data=payload)
                
                time.sleep(0.1)
                
        else:
            contenu = input("\033[32m\n           [+]Input the content of the message.[Want to load the content of a .txt file? Put txt] [>] \033[0m")
            if contenu == 'txt':
                path = input("\033[35m\n           [+]Input the path to the .txt file.[>] \033[0m")
                os.chdir(path)
                file_ipt = input("\033[35m\n           [+]Input the name to the .txt file.(Without the extension!)  [>] \033[0m")
                file = (file_ipt + ".txt")
                file_content=open(file, "r")
                contenu = file_content.read()
                file_content.close()
            webhook = input("\033[36m\n           [+]Input the URL of the webhook. [>] \033[0m")
            spam = input("\033[33m\n           [+]Input the amount of messages that is going to be send. [>] \033[0m")
            tts_statut = input("\033[36m\n           [+]Do you want to make TTS enabled? [Y/N]. [>] \033[0m")
            if tts_statut == "Y":
                tts = "true"
            elif tts_statut == "N":
                tts = "false"
            payload = {
                "content": contenu,
                "tts": tts,
            }
            ctn = 0
            print("\033[32m\n\n           [+]The spam has started. \n\033[0m")
            while ctn<int(spam):
                ctn+=1
                requests.post(webhook, data=payload)
                
                time.sleep(0.1)
            

    
    elif choice == "1":
        clear()
        term()
        
    elif choice == "2":
        terminal = False
        if os.name == 'nt':
            os.system("color 4")
            print("\n                       [+]Goodbye.                      akira")
        else:
            print("\033[33m\n\n                        [+]Goodbye.                           akira\n\n\033[0m")
    else:
        if os.name == 'nt':
            os.system("color 0d")
            print("\n                 This command doesn't exist. Please try another command.\n\n")
        
        else:
            print("\n\033[41m\nThis command doesn't exist. Please try another command.\n\n\033[0m")
            


    
