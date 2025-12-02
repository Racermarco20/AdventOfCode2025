def start(dial_starting_point_user: int = 50):
    zero_count = 0
    dial_starting_point = int(dial_starting_point_user)

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
        end_position = dial_starting_point % 100  # -> 0
        zero_jumped = (dial_starting_point // 100)

        if zero_jumped < 1:
            zero_jumped = zero_jumped * (-1)

        print("Zero Jumped: " + str(zero_jumped))
        print("New position: " + str(end_position))

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
    start(50)
