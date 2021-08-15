import json
from os import path
from colorama import init, Fore

init()
DefaultConfig = {
    "MysqlHost": "CHANGE THIS",
    "MysqlId": "CHANGE THIS",
    "MysqlPw": "CHANGE THIS",
    "MysqlDb": "DEBIAN",
    "Debug": False,
    "MaximumGetScoresCount": 50,
    "Threads": 3
}

class JsonFile:
    @classmethod
    def SaveDict(self, Dict, File="config.json"):
        with open(File, 'w') as json_file:
            json.dump(Dict, json_file, indent=4)

    @classmethod
    def GetDict(self, File="config.json"):
        if not path.exists(File):
            return {}
        else:
            with open(File) as f:
                data = json.load(f)
            return data


Config = JsonFile.GetDict("./config.json")

if Config == {}:
    print(Fore.RED + "Not Found Config" + Fore.RESET)
    JsonFile.SaveDict(DefaultConfig, "./config.json")
    print(Fore.LIGHTYELLOW_EX + "New Config File generated.")
    print(Fore.LIGHTYELLOW_EX + "File Name : config.json")
    exit()
else:
    AllGood = True
    NeedSet = []
    for key in list(DefaultConfig.keys()):
        if key not in list(Config.keys()):
            AllGood = False
            NeedSet.append(key)

    if AllGood:
        print(Fore.GREEN + "Config Loaded" + Fore.RESET)
    else:
        print(Fore.BLUE + " Updating Config" + Fore.RESET)
        for Key in NeedSet:
            Config[Key] = DefaultConfig[Key]
            print(Fore.BLUE + f"{Key} added to config." + Fore.RESET)
        print(Fore.GREEN + "Config updated!" + Fore.RESET)
        JsonFile.SaveDict(Config, "./config.json")
        exit()