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
            return striped_hash
    return None


def process_strings(args):
    for hash in args:
        for needle in args:
            if needle == hash:
                continue
            # got all different chars and respective indexes
            diff_chars = get_difference(hash, needle)
            if len(diff_chars) == 1:
                result = strip_and_compare_strings(hash, needle, diff_chars)
                if result is not None:
                    print(f"Answer: {result}")
                    break


def main(args):
    process_strings(args)


if __name__ == "__main__":
    with open("inputs/input.txt", "r") as r:
        main([line.strip() for line in r.readlines()])
