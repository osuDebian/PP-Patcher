from objects.config import Config
import subprocess
import json
from objects import glob, convertor
from colorama import Fore

def pp_calculator(mapid = 0, mode = "osu", score = 0, acc = 0.0, mods = ("HD", "DT"), combo = 0, x100 = 0, x50 = 0, miss = 0):
    glob.logging(f"{Fore.LIGHTCYAN_EX}[Calculator]{Fore.RESET}", f"command generating....")
    commands = f"./PerformanceCalculator simulate {mode} {str(mapid)} -j {convertor.ConvertCommands(mode, mods, score, acc, combo, x100, x50, miss)}"

    glob.logging(f"{Fore.LIGHTCYAN_EX}[Calculator]{Fore.RESET}", f"command generate successful!: {commands}")
    
    process = subprocess.run(commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = None
    decoding = process.stdout.decode("utf-8")

    try:
        decoding = decoding.replace(f"Downloading {mapid}.osu...", "")
    except:
        pass

    try:
        output = json.loads(decoding)
        if Config["Debug"]:
            glob.logging(f"{Fore.LIGHTCYAN_EX}[Calculator]{Fore.RESET}", "output: ", decoding)
    except (json.JSONDecodeError) as e:
        print(e, decoding)
    return output