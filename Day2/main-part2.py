def start():
    data = load_file()
    data = data.split(',')
    invalid_id_sum = 0

    for i in range(len(data)):
        first_number, last_number = data[i].split('-')
        diff = int(last_number) - int(first_number)

        for j in range(diff + 1):
            current_number = int(first_number) + j
            current_number = str(current_number)
            max_split = len(current_number) // 2
            print("Current number: " + str(current_number))
            print("Number of digits: " + str(len(current_number)) + "")
            print("Max split: " + str(max_split))
            for k in range(max_split):
                splits = [current_number[m:m + k + 1] for m in range(0, len(current_number), k + 1)]

                all_splits_are_identical = all(x == splits[0] for x in splits)
                all_splits_are_identical_long = all(len(y) == len(splits[0]) for y in splits)

                if all_splits_are_identical_long:
                    print("Splits: " + str(splits) + " , Runde: " + str(k + 1))

                if all_splits_are_identical and all_splits_are_identical_long:
                    invalid_id_sum += int(current_number)

            print("----------------------------------------------------------------------------")

    print("Invalid ID Sum: " + str(invalid_id_sum))


def load_file():
    with open("input.txt", "r") as f:
        return f.read()


if __name__ == '__main__':
    start()
