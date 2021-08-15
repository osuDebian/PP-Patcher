import datetime
from objects.config import Config
import pymysql
from pymysql.cursors import Cursor

title_card: str = '''
 ______ ______     ______                _                 
(_____ (_____ \   (_____ \     _        | |                
 _____) )____) )   _____) )___| |_  ____| | _   ____  ____ 
|  ____/  ____/   |  ____/ _  |  _)/ ___) || \ / _  )/ ___)
| |    | |        | |   ( ( | | |_( (___| | | ( (/ /| |    
|_|    |_|        |_|    \_||_|\___)____)_| |_|\____)_|    

-------------------------------------------------------
'''

cur: Cursor = None
conn: pymysql.Connect = None

progressPage = 388
TotalWorksCount = 0

progressPages = []
for i in range(Config["Threads"]):
    progressPages.append(progressPage * (i + 1))

processlist = []

def logging(*val):
    now = datetime.datetime.now()
    nowtime = now.strftime("%Y-%m-%d %H:%M:%S")
    string = ""
    for i in val:
        if i == val[0]:
            string += f"{i}"
        else:
            string += f" {i}"
    print(f"\033[92m{nowtime} \033[0m| \033[0m{string}\033[0m")