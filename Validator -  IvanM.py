import csv

fake = []


def validate(num: str):
    if len(num) == 16:
        num = list(num)
        num.pop(15)
        return True
    else:
        fake.append(num)
    return False


def last_num(num: str):
    last_num = int(num[15])
    if last_num % 2 == 1:
        return True
    return False


def num_0dd(num: str):
    num = int(num[0])
    if num % 2 == 1:
        return True
    return False


def multiply(num: str):
    if num[0: 15] == [1, 3, 5, 7, 9]:
        int(str(num_0dd) * 2)
        if 
        return True
    return False


def reverse(num: str):
    print(num[:: - 1])


with open("Book1.csv", 'r') as old_csv:
    with open(" TheFiles.csv", 'w') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("processing...")

        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
        print("Ok")
