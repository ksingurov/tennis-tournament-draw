from match.utils import build_tournament


if __name__ == "__main__":
    N = 16
    players = list(range(1, N + 1))
    # draw = build_tournament(players=players, max_rounds=2)
    draw = build_tournament(players=players)
    for m in draw:
        print(m)
