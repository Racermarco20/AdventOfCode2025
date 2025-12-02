import math


def start(dial_starting_point_user: int = 50):
    dial_starting_point = int(dial_starting_point_user)
    zero_count = 0

    content = load_file()
    for line in content.splitlines():
        distance = int(line[1:])
        start_postion = dial_starting_point

        if line.startswith("R"):
            zero_count += math.floor(start_postion + distance / 100)
            dial_starting_point = (start_postion + distance) % 100
        elif line.startswith("L"):
            zero_count += math.ceil((start_postion / 100)) - math.ceil((start_postion - distance) / 100)
            dial_starting_point = (start_postion - distance) % 100
    print("Zero Count: " + str(zero_count))


def load_file():
    with open("input.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    start(50)
