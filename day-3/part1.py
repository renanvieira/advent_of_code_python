import re


def create_claims(args):
    claims = list()
    for item in args:
        matches = re.search(r'#(\d+) @ (\d+,\d+): (\d+x\d+)', item)
        coords = matches.groups()[1].split(',')
        size = matches.groups()[2].split('x')

        claim = dict()
        claim["id"] = matches.groups()[0]
        claim["x"] = int(coords[0])
        claim["y"] = int(coords[1])
        claim["width"] = int(size[0])
        claim["height"] = int(size[1])

        claims.append(claim)
    return claims


def main(args):
    claims = create_claims(args)
    claimed = set()
    overlapping = set()

    for claim in claims:
        cur_claimed = set(
            (i + claim["x"], claim["y"] + j) for i in range(claim["width"]) for j in range(claim["height"]))
        overlapping |= cur_claimed & claimed
        claimed |= cur_claimed
    print(f"Number of overlapping claims: {len(overlapping)}")


if __name__ == "__main__":
    with open("inputs/input.txt", "r") as r:
        main([line.strip() for line in r.readlines()])
