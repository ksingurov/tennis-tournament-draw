import os
import re
import json
import sys

def print_usage():
    print(
        "Usage:\n"
        "  python parse_entries_from_text.py <input_txt_file> <output_json_file>\n"
        "Example:\n"
        "  python parse_entries_from_text.py ms_entries_extracted.txt players.json"
)

def main():
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Error: File not found: {input_file}")
        sys.exit(1)

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = r"(\d+)\s+([A-Za-z' -]+),\s+([A-Za-z' -]+)(?:\s+\(([A-Z]{3})\))?(?:\s+([A-Z ]+))?\s+(\d+)"

    player_fields = (
        "entry#",
        "surname",
        "name",
        "country",
        "entry_info",
        "rank"
    )

    players = []
    for m in re.finditer(pattern, text):
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

    players = sorted(players, key=lambda p: p["entry#"] if p["entry#"] is not None else float('inf'))

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(players, f, indent=2)

    print(f"{len(players)} player entries written to: {output_file}")

if __name__ == "__main__":
    main()
