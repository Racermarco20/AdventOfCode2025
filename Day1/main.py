def start(is_part_two: bool = False):
    dial_starting_point = 50
    zero_count = 0

    content = load_file()
    print("Starting point: " + str(dial_starting_point))
    for line in content.splitlines():
        if line.startswith("R"):
            number = line.split("R")[1].strip()
            number = int(number)
            dial_starting_point += number
        elif line.startswith("L"):
            number = line.split("L")[1].strip()
            number = int(number)
            dial_starting_point -= number

        while dial_starting_point < 0:
            dial_starting_point += 100
            if is_part_two:
                zero_count += 1
                print("0 was jumped, add it to count")
        while dial_starting_point > 99:
            dial_starting_point -= 100
            if is_part_two:
                zero_count += 1
                print("0 was jumped, add it to count")

        if dial_starting_point == 0:
            zero_count += 1

        print(str(dial_starting_point) + " ----- " + line)

    print("--------------------")
    print("Zero Count:" + str(zero_count))


def load_file():
    with open("input.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    start(True)
