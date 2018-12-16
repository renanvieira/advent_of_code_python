def get_difference(a, b):
    diff_chars = list()
    for index, char in enumerate(a):
        if char not in b:
            diff_chars.append((char, index))

    return diff_chars


def strip_and_compare_strings(hash, needle, diff_chars):
    if len(diff_chars) > 0:
        diff_tuple = diff_chars[0]

        striped_hash = hash[:diff_tuple[1]] + hash[diff_tuple[1] + 1:]
        striped_needle = needle[:diff_tuple[1]] + needle[diff_tuple[1] + 1:]

        if striped_hash == striped_needle:
            print(f"striped char: {striped_needle}")
            return diff_tuple, True
    return None, False


def process_strings(args):
    diff = list()
    for hash in args:
        for needle in args:
            if needle == hash:
                continue

            # got all different chars and respective indexes
            diff_chars = get_difference(hash, needle)
            if len(diff_chars) == 1:
                tuple, result = strip_and_compare_strings(hash, needle, diff_chars)
                if result is True:
                    diff.append(tuple)
    print(diff)
    return diff


def summerized_diff(diff_list):
    letter_count = dict()
    # search common repetitions
    for item in diff_list:
        for key, val in item.items():
            if key in letter_count:
                letter_count[key] += 1
            else:
                letter_count[key] = 1

    return letter_count


def main(args):
    diff = process_strings(args)

    # summary = summerized_diff(diff)

    # print(f"Repeting summary: {summary}")

    # most_repeting_letter = max(summary.items(), key=operator.itemgetter(1))

    # print("Most repeting letter: {}, {} times".format(most_repeting_letter[0], most_repeting_letter[1]))


if __name__ == "__main__":
    with open("inputs/input.txt", "r") as r:
        main([line.strip() for line in r.readlines()])
