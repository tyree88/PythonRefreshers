def main():
    game = ["rock", "paper", "scissors", "lizard", "spock"]
    gameTuple = ("rock", "computer", "lizard")
    print(game[1:3:2])  # its like range has a step
    i = game.index("paper")
    print_list(game)
    print(game[i])

    x = game.pop()  # returns the last item and removes it
    print_list(game)

    game.append("computer")
    del game[1:3]  # removes a slice # can remove any number of list argument
    game.insert(0, "first")
    print_list(game)

    print(','.join(game))
    print_list(game)

    print_list(gameTuple)


def print_list(a):
    for i in a:
        print(i, end=" ", flush=True)
    print()


if __name__ == "__main__":
    main()
