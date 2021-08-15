from objects import glob
from common.db import dbConnect
from colorama import Fore
from objects.convertor import *
from objects.recalc import *

print(f"\033[94m{glob.title_card}\033[0m")

dbConnect()
if glob.cur is None:
    glob.logging("DB Server Connect Failed")
    exit()
else:
    glob.logging(f"{Fore.LIGHTBLUE_EX}DB Server Connect Successful.")

def ModsSelector():
    val = input(f"Mods Select...\n    1. All Mods\n    2. Regullar Mod Only\n    3. Relax Mod Only\n> ")
    return val

def main():
    val = input(f"Mode Select...\n    1. All Recalc\n    2. Specific User Recalc\n    3. Specific Score Recalc \n> ")

    glob.logging(f"{Fore.LIGHTYELLOW_EX}Select Mode: {ConvertInputMode(val)}")
    if ConvertInputMode(val) == "None":
        glob.logging(f"{Fore.LIGHTRED_EX}Please enter the correct number.")
        return main()
        
    mods = ModsSelector()
    glob.logging(f"{Fore.LIGHTYELLOW_EX}Select Mods: {ConvertInputMods(val)}")
    if ConvertInputMods(val) == "None":
        glob.logging(f"{Fore.LIGHTRED_EX}Please enter the correct number.")
        return main()

    if val == '1':
        return allRecalc(mods)
    elif val == '2':
        return specificUserRecalc(mods)
    elif val == '3':
        return specificScoreRecalc(mods)
    else:
        return main()
        
if __name__ == "__main__":
    main()