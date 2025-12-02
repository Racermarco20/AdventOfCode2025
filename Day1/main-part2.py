import math


def start(dial_starting_point_user: int = 50):
    zero_count = 0
    dial_starting_point = int(dial_starting_point_user)

    content = load_file()
    print("Starting point: " + str(dial_starting_point))
    print("--------------------")
    for line in content.splitlines():
        number = int(line[1:])
        print("Rotate " + line + " beginning from " + str(dial_starting_point) + "")
        zero_count_dummy = 0
        if line.startswith("R"):
            current_position = dial_starting_point + number
            end_position = (current_position % 100)
            zero_count_dummy += (current_position // 100)
        elif line.startswith("L"):
            current_position = dial_starting_point - number
            end_position = (current_position % 100)
            if current_position == 0 or end_position == 0:
                zero_count_dummy += 1
            zero_count_dummy += math.ceil((current_position / -100))
            if dial_starting_point == 0:
                zero_count_dummy -= 1

            print("Zero Count dummy: " + str(zero_count_dummy) + "")

        print("Zero Count in this round: " + str(zero_count_dummy) + "")
        zero_count += zero_count_dummy

        dial_starting_point = end_position
        print("New position: " + str(dial_starting_point))
        print("New Zero Count: " + str(zero_count))
        print("\n")

    print("--------------------")
    print("Zero Count: " + str(zero_count))


def load_file():
    with open("input.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    start(50)
