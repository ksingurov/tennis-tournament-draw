N_PLAYERS = 128

SEEDS_TIERS = {
    1: [1, 2],
    2: [3, 4],
    3: [5, 8],
    4: [9, 12],
    5: [13, 16],
    6: [17, 24],
    7: [25, 32]
}

SEEDED_DRAW_POSITIONS = {
    1: [1, 128],
    2: [33, 96],
    3: [32, 64, 65, 97],
    4: [17, 49, 80, 112],
    5: [16, 48, 81, 113],
    6: [9, 24, 41, 56, 73, 88, 105, 120],
    7: [8, 25, 40, 57, 72, 89, 104, 121]
}

# all_seeded_positions = [pos for bracket in SEEDED_DRAW_POSITIONS.values() for pos in bracket]
# unseeded_draw_positions = list(set(range(1, N_PLAYERS + 1)) - set(all_seeded_positions))
# # print(unseeded_draw_positions)

# tiers = {}
# for t in SEEDS_TIERS.keys():
#     seeds = list(range(SEEDS_TIERS[t][0], SEEDS_TIERS[t][1] + 1))
#     positions = SEEDED_DRAW_POSITIONS[t]
#     tiers[t] = (seeds, positions)


# if __name__ == "__main__":
#     for key, value in tiers.items():
#         print(f"key: {key}, value: {value}")
