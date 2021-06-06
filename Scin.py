import math
import time
import os
def cls():

  os.system('cls' if os.name=='nt' else 'clear')
from colorama import Fore, Back, Style
cls()
qewsd = """
╭━━━┳╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━━┫┃╱╱╱╱╱╭╯╰╮╱╱╱╱╱╱╱╱╱┃┃
┃╰━━┫┃╭━━┳━┻╮╭╋━┳┳━━╮╭━━┫╰━┳━━┳━┳━━┳━━╮
┃╭━━┫┃┃┃━┫╭━┫┃┃╭╋┫╭━╯┃╭━┫╭╮┃╭╮┃╭┫╭╮┃┃━┫
┃╰━━┫╰┫┃━┫╰━┫╰┫┃┃┃╰━╮┃╰━┫┃┃┃╭╮┃┃┃╰╯┃┃━┫
╰━━━┻━┻━━┻━━┻━┻╯╰┻━━╯╰━━┻╯╰┻╯╰┻╯╰━╮┣━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰
Calculator 
Author: @Callstodev1(Pulatov Kamran)
"""
print(qewsd)

# This programm created by Pulatov Kamran :D
# My program is designed only for static electricity calculations 
# if you don't know using my programm, please don't using my programm

#          _____                    _____                    _____                    _____                    _____                    _____          
#         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
#        /::\____\                /::\    \                /::\____\                /::\    \                /::\    \                /::\____\        
#       /:::/    /               /::::\    \              /::::|   |               /::::\    \              /::::\    \              /::::|   |        
#      /:::/    /               /::::::\    \            /:::::|   |              /::::::\    \            /::::::\    \            /:::::|   |        
#     /:::/    /               /:::/\:::\    \          /::::::|   |             /:::/\:::\    \          /:::/\:::\    \          /::::::|   |        
#    /:::/____/               /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \        /:::/__\:::\    \        /:::/|::|   |        
#   /::::\    \              /::::\   \:::\    \      /:::/ |::|   |           /::::\   \:::\    \      /::::\   \:::\    \      /:::/ |::|   |        
#  /::::::\____\________    /::::::\   \:::\    \    /:::/  |::|___|______    /::::::\   \:::\    \    /::::::\   \:::\    \    /:::/  |::|   | _____  
# /:::/\:::::::::::\    \  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \  /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \ 
#/:::/  |:::::::::::\____\/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\/:::/  \:::\   \:::|    |/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\
#\::/   |::|~~~|~~~~~     \::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /\::/   |::::\  /:::|____|\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /
# \/____|::|   |           \/____/ \:::\/:::/    /  \/____/      /:::/    /  \/____|:::::\/:::/    /  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    / 
#       |::|   |                    \::::::/    /               /:::/    /         |:::::::::/    /            \::::::/    /           |::|/:::/    /  
#       |::|   |                     \::::/    /               /:::/    /          |::|\::::/    /              \::::/    /            |::::::/    /   
#       |::|   |                     /:::/    /               /:::/    /           |::| \::/____/               /:::/    /             |:::::/    /    
#       |::|   |                    /:::/    /               /:::/    /            |::|  ~|                    /:::/    /              |::::/    /     
#       |::|   |                   /:::/    /               /:::/    /             |::|   |                   /:::/    /               /:::/    /      
#       \::|   |                  /:::/    /               /:::/    /              \::|   |                  /:::/    /               /:::/    /       
#        \:|   |                  \::/    /                \::/    /                \:|   |                  \::/    /                \::/    /        
#         \|___|                   \/____/                  \/____/                  \|___|                   \/____/                  \/____/         


#                                 .d8888.  .o88b. d888888b d88888b d8b   db  .o88b. d88888b             @@@ #######
#                                 88'  YP d8P  Y8   `88'   88'     888o  88 d8P  Y8 88'                 @@@ ###   ###
#                                 `8bo.   8P         88    88ooooo 88V8o 88 8P      88ooooo                 ###     ###
#                                   `Y8b. 8b         88    88~~~~~ 88 V8o88 8b      88~~~~~                 ###     ///
#                                 db   8D Y8b  d8   .88.   88.     88  V888 Y8b  d8 88.                 @@@ ###    ##
#                                 `8888Y'  `Y88P' Y888888P Y88888P VP   V8P  `Y88P' Y88888P             @@@ ########
                                                         
                                                         



try:
    while True:
    
        qws = input("choose: \n[1]Найти силу воздействия\n[2]найти кол-во заряда если q1=q2\n[3]Найти расстояние между двумя частицами\n[4] найти q1\n[5] Найти q2\n> " )
        if qws == "1":

           a = float(input("Введите q1: "))
           c = float(input("Введите q2: "))
           d = float(input("Введите r: "))

           rab = 9000000000 * math.fabs(a) * math.fabs(c)
           X = d ** 2
           otv = rab / X

           print("calculating...")
           time.sleep(2)
  
           print(Fore.GREEN + "Answer " + str(otv) + " ~ " + str(round(otv)))
           print(Fore.WHITE + "")
           print("==========================================================")

        elif qws == "2":
        
           a = float(input("Введите силу взаимодействия F: "))
           c = float(input("Ведите r: "))

           X = c ** 2
           qw = a * X
           otv = qw / 9000000000

           q = math.sqrt(otv)

           print("calculating...")
           time.sleep(2)
        
           print(Fore.GREEN + "Answer " + str(q) + " ~ " + str(round(otv))) 
           print(Fore.WHITE + "")
           print("========================================================")

        elif qws == "3":  
           a = float(input("Введите q1: "))
           s = float(input("Введите q2: "))
           F = float(input("Введите F: "))

           asq = 9000000000
           q12 = asq * a * s 
           otv1 = q12 / F 
           otv = math.sqrt(otv1)

           print("calculating...")
           time.sleep(2)
        
           print(Fore.GREEN + "Answer " + str(otv) + " ~ " + str(round(otv))) 
           print(Fore.WHITE + "")
           print("==========================================================")

        elif qws == "4":

           a = float(input("Введите q2: "))
           b = float(input("Введите F: "))
           c = float(input("Введите r: "))
        
           c1 = c ** 2
           x1 = b * c1 
           asq = 9000000000
           z = asq * a 
           otv = x1 / z

           print("calculating...")
           time.sleep(2)
        
           print(Fore.GREEN + "Answer " + str(otv) + " ~ " + str(round(otv))) 
           print(Fore.WHITE + "")
           print("===========================================================")

        elif qws == "5":
         
           a = float(input("Введите q1: "))
           b = float(input("Введите F: "))
           c = float(input("Введите r: "))
        
           c1 = c ** 2
           x1 = b * c1 
           asq = 9000000000
           z = asq * a 
           otv = x1 / z

           print("calculating...")
           time.sleep(2)
        
           print(Fore.GREEN + "Answer " + str(otv) + " ~ " + str(round(otv)))    
           print(Fore.WHITE + "")
           print("==========================================================")

        else:
           print(Fore.RED + "ERROR OPERATION!") 
           print(Fore.WHITE + "")   

except KeyboardInterrupt:
    print(" \n Bye don't cry")