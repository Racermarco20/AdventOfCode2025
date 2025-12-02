def start(is_part_two: bool = False, dial_starting_point_user: int = 50):
    zero_count = 0
    dial_starting_point = int(dial_starting_point_user)
    is_zero = False

    content = load_file()
    print("Starting point: " + str(dial_starting_point))
    print("--------------------")
    for line in content.splitlines():
        number = int(line[1:])
        print("Rotate " + line + " beginning from " + str(dial_starting_point) + "")

        if line.startswith("R"):
            dial_starting_point += number
        elif line.startswith("L"):
            dial_starting_point -= number

        zero_jumped = 0

        while dial_starting_point < 0:
            dial_starting_point += 100
            zero_jumped += 1
            print("Zero jumped: " + str(zero_jumped))
        while dial_starting_point > 100:
            dial_starting_point -= 100
            zero_jumped += 1
            print("Zero jumped: " + str(zero_jumped))

        if dial_starting_point == 100: dial_starting_point = 0

        print("New position: " + str(dial_starting_point))

        if dial_starting_point == 0:
            print("0 reached, add it to count")
            zero_count += 1
        if is_part_two:
            zero_count += zero_jumped
        print("New Zero Count: " + str(zero_count))
        print("\n")

    print("--------------------")
    print("Zero Count: " + str(zero_count))


def load_file():
    with open("input.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    start(True, 14)
