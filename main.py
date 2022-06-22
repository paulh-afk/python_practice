def toCSV(liste):
    csv = ""
    for i in range(len(liste)):
        values = list(liste[i].items())

        if(i == 0):
            for k in range(len(values)):
                csv += values[k][0]
                if (k != (len(values) - 1)):
                    csv += ","
            csv += "\n"

        for j in range(len(values)):
            if(j != 0):
                csv += ","
            csv += str(list(values)[j][1])

        if (i != (len(liste) - 1)):
            csv += "\n"
    return csv


my_liste = [{"name": "Paul", "age": "12", "isAdult": False}, {
    "name": "Josh", "age": "14", "isAdult": False}, {"name": "Daniel", "age": "22", "isAdult": True}]

csv_content = toCSV(my_liste)
print(csv_content)
