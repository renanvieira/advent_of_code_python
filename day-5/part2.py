import re
import string


def has_reaction(unit_a, unit_b):
    opposite = (unit_a.lower() == unit_b.lower() and
                (
                        (unit_a.isupper() and unit_b.islower())
                        or
                        (unit_a.islower() and unit_b.isupper())
                ))

    return opposite


def start_reactions(polymer):
    polymer_after_reaction = []
    for unit in polymer:
        if polymer_after_reaction and has_reaction(unit, polymer_after_reaction[-1]):
            polymer_after_reaction.pop()
        else:
            polymer_after_reaction.append(unit)
    return polymer_after_reaction


def main(polymer):
    reductions = list()
    for char in string.ascii_lowercase:
        new_polymer = re.sub(char, '', polymer[0], flags=re.IGNORECASE)
        polymer_after_reaction = start_reactions(new_polymer)

        reductions.append(len(polymer_after_reaction))

    print(f"Answer: {sorted(reductions)[0]}")


if __name__ == "__main__":
    with open("inputs/input.txt", "r") as r:
        main([line.strip() for line in r.readlines()])
