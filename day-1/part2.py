def main(args):
    result = 0
    past_frequencies = set()
    duplicate_found = False
    while duplicate_found is False:
        for num in args:
            print("Current Frenquency: {}, change of {}; resulting frequency: {}".format(result, "%+d" % num,
                                                                                         result + num))
            result += num

            if result in past_frequencies:
                duplicate_found = True
                print("- First repeating frequency: {}".format(result))
                break
            else:
                past_frequencies.add(result)


if __name__ == "__main__":
    with open("inputs/input4", "r") as r:
        main([int(item.strip()) for item in r.readlines()])
