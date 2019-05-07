import csv

fake = []


def validate(num: str):
    if len(num) == 16:
        last_num = num[15]
        num = list(num)
        num.pop(15)
        reverse_version = reverse_num(num)
        for index in range(len(reverse_version)):
            reverse_version[index] = int(reverse_version[index])

        new_list = multiply(reverse_version)
        if int(last_num) == add_all_num(new_list) % 10:
            return True
    else:
        fake.append(num)
    return False


def multiply(num: list):
    for index in range(len(num)):
        if index % 2 == 0:
            num[index] *= 2
        if num[index] > 9:
            num[index] -= 9
        return num


def reverse(num: list):
    print(num[:: - 1])


def add_all_num(num: list):
    add = (num[0] + num[1] + num[2] + num[3] + num[4] + num[5] + num[6] + num[7] + num[8] + num[9] + num[10] + num[12]
           + num[13] + num[14])
    return add


with open("Book1.csv", 'r') as old_csv:
    with open(" TheFiles.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("processing...")

        for row in reader:
            old_number = row[0]
            first_num = int(old_number[0])
            if validate(old_number):
                writer.writerow(row)
        print("Ok")
