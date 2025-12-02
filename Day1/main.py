def start(is_part_two: bool = False, dial_starting_point_user: int = 50):
    zero_count = 0
    dial_starting_point = int(dial_starting_point_user)
    ignore_zero = False

    content = load_file()
    print("Starting point: " + str(dial_starting_point))
    print("--------------------")
    for line in content.splitlines():
        number = int(line[1:])
        print("Rotate " + line + " beginning from " + str(dial_starting_point) + "")

        dial_starting_point_mod = dial_starting_point

        if line.startswith("R"):
            dial_starting_point += number
        elif line.startswith("L"):
            dial_starting_point -= number
        end_position = dial_starting_point % 100
        print("End position: " + str(end_position))
        zero_jumped = (dial_starting_point // 100)

        if zero_jumped < 1:
            zero_jumped = zero_jumped * (-1)
        print("Dial starting point: " + str(dial_starting_point_mod) + "")
        if dial_starting_point_mod == 0:
            zero_jumped -= 1
            if zero_jumped < 0: zero_jumped = 0

        print("Zero Jumped: " + str(zero_jumped))

        if zero_jumped == 1 and end_position == 0:
            ignore_zero = True
        print("New position: " + str(end_position))

        if end_position == 0:
            print("0 reached, add it to count")
            zero_count += 1
        if is_part_two and not ignore_zero:
            zero_count += zero_jumped
        dial_starting_point = end_position
        print("New Zero Count: " + str(zero_count))
        print("\n")

    print("--------------------")
    print("Zero Count: " + str(zero_count))


def load_file():
    with open("input.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    start(True, 50)
