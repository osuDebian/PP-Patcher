from objects import glob, calculator, convertor, config
from colorama import Fore
import time

def getScores(mods, pmultiplier):
    glob.logging(f"{Fore.LIGHTRED_EX}[Thread #{pmultiplier}]{Fore.RESET}", 'Preparing Get Scores...')
    if mods == '1' or mods == '2':
        glob.cur.execute(f"select id, beatmap_id, beatmap_md5, userid, score, max_combo, mods, 300_count, 100_count, 50_count, misses_count, play_mode, accuracy, pp from scores where play_mode = 0 and pp > 0 order by id asc limit {glob.progressPages[pmultiplier - 1] * config.Config['MaximumGetScoresCount']}, {config.Config['MaximumGetScoresCount']};")
        scores = glob.cur.fetchall()
    elif mods == '3' or mods == '4':
        glob.cur.execute(f"select id, beatmap_id, beatmap_md5, userid, score, max_combo, mods, 300_count, 100_count, 50_count, misses_count, play_mode, accuracy, pp from scores_relax where play_mode = 0 and pp > 0 order by id asc limit {glob.progressPages[pmultiplier - 1] * config.Config['MaximumGetScoresCount']}, {config.Config['MaximumGetScoresCount']};")
        scores = glob.cur.fetchall()
    glob.logging(f"{Fore.LIGHTRED_EX}[Thread #{pmultiplier}]{Fore.RESET}", f'Successfully get scores! {Fore.LIGHTYELLOW_EX}scores count: {len(scores)} {Fore.LIGHTMAGENTA_EX}now Page: {glob.progressPages[pmultiplier - 1] + 1}')
    glob.progressPages[pmultiplier - 1] += 1
    return scores

def commitScores(mods: str, data: dict, pmultiplier):
    glob.logging(f"{Fore.LIGHTRED_EX}[Thread #{pmultiplier}]{Fore.RESET}", 'Commiting Scores...')
    if mods == '1' or mods == '2':
        glob.cur.execute(f"update scores set pp = {data['pp']} where id = {data['score_id']}")
        glob.conn.commit()
    elif mods == '3' or mods == '4':
        glob.cur.execute(f"update scores_relax set pp = {data['pp']} where id = {data['score_id']}")
        glob.conn.commit()
    glob.logging(f"{Fore.LIGHTRED_EX}[Thread #{pmultiplier}]{Fore.RESET}", f"Committed!", f"score id {data['score_id']}'s pp has been Changed: {Fore.LIGHTYELLOW_EX}{data['old_pp']}pp -> {data['pp']}pp")
    glob.logging(f"{Fore.LIGHTRED_EX}[Thread #{pmultiplier}]{Fore.RESET}", f"    Now Working:::::: Total Works: {glob.TotalWorksCount}")

def allRecalc(mods, pmultiplier):
    start = time.perf_counter()
    scores = getScores(mods, pmultiplier)
    if len(scores) < config.Config['MaximumGetScoresCount'] and mods == "1":
        glob.logging(f"{Fore.LIGHTRED_EX}[Thread #{pmultiplier}]{Fore.RESET}", f"Regullar Mode's All scores have been recalcuated! and now, Relax Mode's scores recalcuate has been start.\n    Total Works: {glob.TotalWorksCount}")
        glob.progressPage = 0
        return allRecalc('4', pmultiplier)
    elif len(scores) < config.Config['MaximumGetScoresCount'] and mods != "1":
        glob.logging(f"{Fore.LIGHTRED_EX}[Thread #{pmultiplier}]{Fore.RESET}", f"Work Done.\n    Total Works: {glob.TotalWorksCount}")
        exit()
    for s in scores:
        if not s[1] == 0:
            newPP = calculator.pp_calculator(mapid=s[1], mode=convertor.ConvertMode(s[11]), score=s[4], acc=s[12], mods=convertor.ConvertMods(s[6]), combo=s[5], x100=s[8], x50=s[9], miss=s[10])
            if newPP != None:
                newPP['score_id'] = s[0]
                newPP['user_id'] = s[3]
                newPP['old_pp'] = s[13]
                commitScores(mods, newPP, pmultiplier)
                glob.TotalWorksCount += 1
            else:
                pass
    finish = time.perf_counter()
    glob.logging(f"{Fore.LIGHTRED_EX}[Thread #{pmultiplier}]{Fore.RESET}", f"All scores have been recalculated. ({round(finish-start,2)}s) Trying to get next scores..")
    return allRecalc(mods, pmultiplier)

def specificUserRecalc(mods):
    glob.logging('g2g2g2')

def specificScoreRecalc(mods):
    glob.logging('g2g2g2')