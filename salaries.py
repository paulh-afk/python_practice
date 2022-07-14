import csv

with open("./input.csv", "r") as input_file:
    reader = csv.DictReader(input_file, delimiter=',')
    names = []
    salaries = []

    for line in reader:
        names.append(line["nom"])
        salaries.append(int(line["heures_travaillees"]) * 15)

    header = ["nom", "salaire"]

    with open("./output.csv", "w") as output_file:
        writer = csv.writer(output_file, delimiter=",")
        writer.writerow(header)

        for name, salary in zip(names, salaries):
            writer.writerow([name, salary])
