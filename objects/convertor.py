NoFail = 1
Easy = 2
NoVideo = 4
Hidden = 8
HardRock = 16
SuddenDeath = 32
DoubleTime = 64
Relax = 128
HalfTime = 256
Nightcore = 512
Flashlight = 1024
Autoplay = 2048
SpunOut = 4096
Relax2 = 8192
Perfect = 16384
Key4 = 32768
Key5 = 65536
Key6 = 131072
Key7 = 262144
Key8 = 524288
keyMod = 1015808
FadeIn = 1048576
Random = 2097152
LastMod = 4194304
Key9 = 16777216
Key10 = 33554432
Key1 = 67108864
Key2 = 268435456
Key3 = 134217728
SCOREV2 = 536870912

def ConvertInputMode(val):
    if val == '1':
        return "All Recalc"
    elif val == '2':
        return "Specific User Recalc"
    elif val == '3':
        return "Specific Score Recalc"
    else:
        return "None"

def ConvertInputMods(val):
    if val == '1':
        return "All Mods"
    elif val == '2':
        return "Regullar Mod Only"
    elif val == '3':
        return "Relax Mod Only"
    else:
        return "None"

def ConvertMode(m):
    if m == 0 or m == '0':
        return "osu"
    elif m == 1 or m == '1':
        return 'taiko'
    elif m == 2 or m == '2':
        return 'catch'
    elif m == 3 or m == '3':
        return 'mania'
    else:
        return 'osu'

def ConvertMods(m):
    r = []
    hasNightcore = False
    hasPF = False
    if m & Easy:
        r.append("NF")
    if m & NoFail:
        r.append("NF")
    if m & HalfTime:
        r.append("HT")
    if m & HardRock:
        r.append("HR")
    if m & Perfect:
        hasPF = True
        r.append("PF")
    if m & SuddenDeath and hasPF == False:
        r.append("SD")
    if m & Nightcore:
        r.append("NC")
        hasNightcore = True
    if m & DoubleTime and hasNightcore == False:
        r.append("DT")
    if m & Hidden:
        r.append("HD")
    if m & Flashlight:
        r.append("FL")
    if m & Random:
        r.append("RD")
    if m & Autoplay:
        r.append("AT")
    if m & SpunOut:
        r.append("SO")
    if m & Relax:
        r.append("RX")
    if m & Relax2:
        r.append("AP")
    if m & Key1:
        r.append('1K')
    if m & Key2:
        r.append('2K')
    if m & Key3:
        r.append('3K')
    if m & Key4:
        r.append('4K')
    if m & Key5:
        r.append('5K')
    if m & Key6:
        r.append('6K')
    if m & Key7:
        r.append('7K')
    if m & Key8:
        r.append('8K')
    if m & Key9:
        r.append('9K')
    if m & Key10:
        r.append('10K')
    if m & keyMod:
        r.append("")
    if m & LastMod:
        r.append("CN")
    if m & SCOREV2:
        r.append("V2")
    if len(r) > 0:
        return r
    else:
        return []

def ConvertCommands(m, mods, score, acc, combo, x100, x50, miss):
    commands = ""
    if m == "osu" or m == 0:
        commands += f"-a {acc} -c {combo} -G {x100} -M {x50} -X {miss}"
    if m == "taiko" or m == 1:
        commands += f"-a {acc} -c {combo} -G {x100} -X {miss}"
    if m == "catch" or m == 2:
        commands += f"-a {acc} -c {combo} -D {x100} -T {x50} -X {miss}"
    if m == "maina" or m == 3:
        commands += f"-s {score}"
    for i in mods:
        commands += f" -m {i}"
    return commands