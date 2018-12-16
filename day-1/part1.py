def main(args):
    result = sum(args)
    print(result)


if __name__ == "__main__":
    with open("inputs/input", "r") as r:
        print("Input 1: ")
        main([int(item.strip()) for item in r.readlines()])

    with open("inputs/input2", "r") as r:
        print("Input 2: ")
        main([int(item.strip()) for item in r.readlines()])

    with open("inputs/input3", "r") as r:
        print("Input 3: ")
        main([int(item.strip()) for item in r.readlines()])

    with open("inputs/input4", "r") as r:
        print("Input 4: ")
        main([int(item.strip()) for item in r.readlines()])
