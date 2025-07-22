import os
import re
import json
import sys

def print_usage():
    print(
        "Usage:\n"
        "  python parse_entries_from_text.py <input_txt_file> <file_with_pattern> <file_with_fields> <output_json_file>\n"
        "Example:\n"
        "  python parse_entries_from_text.py ms_entries_extracted.txt pattern.txt fields.txt players.json"
)

def main():
    if len(sys.argv) != 5:
        print_usage()
        sys.exit(1)

    input_file = sys.argv[1]
    pattern_file = sys.argv[2]
    fields_file = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.isfile(input_file):
        print(f"Error: File not found: {input_file}")
        sys.exit(1)

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    with open(pattern_file, "r", encoding="utf-8") as f:
        pattern = f.read().strip()

    with open(fields_file, "r", encoding="utf-8") as f:
        player_fields = tuple(json.load(f))

    players = []
    for m in re.finditer(pattern, text):
        player_record = tuple(g if g != '' else None for g in m.groups())
        p = dict(zip(player_fields, player_record))
        # print(f"[DEBUG] player: {p}")
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
