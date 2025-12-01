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

        while dial_starting_point < 0: dial_starting_point += 100
        while dial_starting_point > 99: dial_starting_point -= 100

        if dial_starting_point == 0:
            zero_count += 1

        print(str(dial_starting_point) + " ----- " + line)

    print("--------------------")
    print("Zero Count:" + str(zero_count))


def load_file():
    with open("input.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    start()
