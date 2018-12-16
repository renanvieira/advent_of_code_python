def main(args):
    counting_dict = dict()
    sum_three = 0
    sum_two = 0

    for item in args:
        counting_dict = dict()

        for char in item:
            if char in counting_dict.keys():
                counting_dict[char] += 1
            else:
                counting_dict[char] = 1

        if 3 in counting_dict.values():
            sum_three += 1

        if 2 in counting_dict.values():
            sum_two += 1

    print("Number with two: {}".format(sum_two))
    print("Number with three: {}".format(sum_three))
    print("Checksum: {}".format(sum_two * sum_three))


if __name__ == "__main__":
    with open("inputs/input.txt", "r") as r:
        main([line.strip() for line in r.readlines()])
