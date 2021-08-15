import pymysql
from objects.config import Config
from colorama import Fore
from objects import glob

def dbConnect():
    try:
        conn = pymysql.connect(host=Config["MysqlHost"], user=Config["MysqlId"], password=Config["MysqlPw"], db=Config["MysqlDb"], charset='utf8mb4')
    except Exception as e:
        glob.logging(f"{Fore.RED}DB Server Connect Failed")
        exit()
    cur = conn.cursor()
    glob.cur = cur
    glob.conn = conn
    