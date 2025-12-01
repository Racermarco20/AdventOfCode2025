def start():
    dial_starting_point = 50
    zero_count = 0

    content = load_file()
    for line in content.splitlines():
        number = 0
        if line.startswith("R"):
            number = line.split("R")[1].strip()
            number = int(number)
            dial_starting_point += number
        elif line.startswith("L"):
            number = line.split("L")[1].strip()
            number = int(number)
            dial_starting_point -= number

        if dial_starting_point > 99:
            rest = 99 - number
            dial_starting_point = rest - 1
        elif dial_starting_point < 0:
            rest = 99 - number
            dial_starting_point = rest + 2

        if dial_starting_point == 0:
            zero_count += 1

        print(dial_starting_point)

    print(zero_count)


def load_file():
    with open("input.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    start()
