import subprocess
import json
from objects import glob

mapid = "1816243"
mode = "osu"
acc = "99.004974"
mods = ("RX", "HD", "DT")
combo = "551"
x100 = "6"
x50 = "0"
miss = "0"

commands = f"./PerformanceCalculator simulate {mode} {mapid} "
commands += f"-j -a {acc} -c {combo} -G {x100} -M {x50} -X {miss}"
for i in mods:
    commands += f" -m {i}"

glob.logging(f"command: {commands}")


process = subprocess.run(commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = None
try:
    decoding = process.stdout.decode("utf-8")
    output = json.loads(decoding)
    glob.logging("output: ", decoding)
except (json.JSONDecodeError, IndexError) as e:
    print(e)

glob.logging(f"PP:", output['pp'])