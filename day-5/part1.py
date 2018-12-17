def has_reaction(unit_a, unit_b):
    opposite = (unit_a.lower() == unit_b.lower() and
                (
                        (unit_a.isupper() and unit_b.islower())
                        or
                        (unit_a.islower() and unit_b.isupper())
                ))

    return opposite


def main(polymer):
    polymer_after_reaction = []
    for unit in polymer[0]:
        if polymer_after_reaction and has_reaction(unit, polymer_after_reaction[-1]):
            polymer_after_reaction.pop()
        else:
            polymer_after_reaction.append(unit)

    print(f"Polymer after reactions: {''.join(polymer_after_reaction)}")
    print("--------------------------")
    print(f"{len(polymer_after_reaction)} units")


if __name__ == "__main__":
    with open("inputs/input.txt", "r") as r:
        main([line.strip() for line in r.readlines()])
