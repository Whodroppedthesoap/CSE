import csv


def validate(num: str):
    first_num = int(num[0])
    if first_num == 0:
        return True
    return False


with open("Book1.csv", 'r') as old_csv:
    with open(" MyNewFile.csv", 'w') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("processing...")

        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
        print("Ok")
