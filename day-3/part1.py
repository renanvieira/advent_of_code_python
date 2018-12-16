def main(args):
    pass


if __name__ == "__main__":
    with open("inputs/input.txt", "r") as r:
        main([line.strip() for line in r.readlines()])
