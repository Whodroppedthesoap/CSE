import csv

fake = []


def validate(num: str):
    if len(num) == 16:
        last_num = int(num[15])
        num -= last_num


def reverse(num: str):
    print(num[:: - 1])


def last_num(num: str):
    last_num = int(num[15])
    if last_num == :
        return True
    return False


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
