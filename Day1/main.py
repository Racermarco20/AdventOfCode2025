def start(is_part_two: bool = False, dial_starting_point_user: int = 50):
    zero_count = 0
    dial_starting_point = int(dial_starting_point_user)
    is_zero = False

    content = load_file()
    print("Starting point: " + str(dial_starting_point))
    print("--------------------")
    for line in content.splitlines():
        number = int(line[1:])

        if dial_starting_point == 0:
            is_zero = True

        if line.startswith("R"):
            dial_starting_point += number
        elif line.startswith("L"):
            dial_starting_point -= number

        print("Rotate " + line + " new position:")

        while dial_starting_point < 0:
            dial_starting_point += 100
            if is_part_two and not is_zero:
                zero_count += 1
                print("0 was jumped, add it to count")
        while dial_starting_point > 99:
            dial_starting_point -= 100
            if is_part_two and not is_zero:
                zero_count += 1
                print("0 was jumped, add it to count")

        is_zero = False

        if dial_starting_point == 0:
            print("0 reached, add it to count")
            zero_count += 1
        print(str(dial_starting_point))
        print("New Zero Count: " + str(zero_count))
        print("\n")

    print("--------------------")
    print("Zero Count:" + str(zero_count))


def load_file():
    with open("input.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    start(True, 50)
