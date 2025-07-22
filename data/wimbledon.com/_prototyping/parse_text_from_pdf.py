import os
import re
import json
# print(os.getcwd())

# Get the absolute path to the script file
script_dir = os.path.dirname(os.path.abspath(__file__))

file_name = 'ms_entries_extracted.txt'
file_path = os.path.join(script_dir, file_name)

with open(file_path, "r") as f:
    text = f.read()

# print(text)

pattern_with_capturing_groups = r"(\d+)\s+([A-Za-z' -]+),\s+([A-Za-z' -]+)(?:\s+\(([A-Z]{3})\))?(?:\s+([A-Z ]+))?\s+(\d+)"

player_fields = (
    "entry#",
    "surname",
    "name",
    "country",
    "entry_info",
    "rank"
)

# matches = re.findall(pattern=pattern, string=text)
# matches = re.findall(pattern=pattern_with_capturing_groups, string=text)
# print(type(matches))
# print(len(matches))
# print(type(matches[0]))
# [g for m in matches for g in m]
# for m in matches:
#     print(m)


players = []
for m in re.finditer(pattern=pattern_with_capturing_groups, string=text):
    player_record = tuple(g if g != '' else None for g in m.groups())
    p = dict(zip(player_fields, player_record))
    try:
        p["entry#"] = int(p["entry#"])
    except ValueError:
        p["entry#"] = None
    try:
        p["rank"] = int(p["rank"])
    except ValueError:
        p["rank"] = None
    players.append(p)
players = sorted(players, key=lambda p: p["entry#"])

# for p in players:
#     print(p)

output_txt = "players.json"
output_txt_path = os.path.join(script_dir, output_txt)
with open(output_txt_path, "w", encoding="utf-8") as f:
    json.dump(players, f, indent=2)
