def start():
    data = load_file()
    data = data.split(',')
    invalid_id_sum = 0

    for i in range(len(data)):
        first_number, last_number = data[i].split('-')
        diff = int(last_number) - int(first_number)

        for j in range(diff):
            current_number = int(first_number) + j
            current_number = str(current_number)
            first_half, second_half = current_number[
                :len(current_number) // 2 + len(current_number) % 2], current_number[
                len(current_number) // 2 + len(current_number) % 2:]

            if first_half == second_half:
                invalid_id_sum += int(current_number)
                print("First half: " + first_half + " Second half: " + second_half)

    print("Invalid ID Sum: " + str(invalid_id_sum))


def load_file():
    with open("input.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    start()
