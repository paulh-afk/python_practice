def toCSV(liste):
    csv = ""
    for i in range(len(liste)):
        values = liste[i].values()

        for j in range(len(values)):
            if(j != 0):
                csv += ","
            csv += list(values)[j]

        if (i != (len(liste) - 1)):
            csv += "\n"
    return csv


my_liste = [{"name": "Paul", "age": "12"}, {
    "name": "Josh", "age": "14"}, {"name": "Daniel", "age": "22"}]

csv_content = toCSV(my_liste)
print(csv_content)
