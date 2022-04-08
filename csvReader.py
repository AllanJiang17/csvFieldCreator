import csv
import getopt


def csvReader(argv):
    fileName = None;
    filePath = None;

    try:
        opts, args = getopt.getopt(argv, "f:p:")

    except:
        print("missing arguments")

    for opt, arg in opts:
        if opt == "-f":
            fileName = arg
        else:
            filePath = arg

    with open(filePath + "\\" + fileName) as file:
        csv_reader = csv.reader(file)
        line = 0
        for row in csv_reader:
            if line != 0:
                type = None
                if "VARCHAR" in row[1]:
                    type = "String"
                elif "number" in row[1]:
                    type = "BigDecimal"
                print("private", type, row[0])
            else:
                line += 1
