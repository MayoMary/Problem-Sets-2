# Mary McHale, 27th March 2018
# Exercise 5 based on Iris Data, studies of the Iris flower by Ronald Fischer in 1936
# Asked to " Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. That is, on the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns.""
# Source of Iris dataset was https://en.wikipedia.org/wiki/Iris_flower_data_set

f = open('data/iris.csv' , 'r')
# This opens the file called iris.csv

print("pl  pw  sl  sw")
# pl = short for Petal length
# pw = short for Petal width
# sl = short for Sepal length
# sw = short for Sepal width

c = 1
record = ""
while c < 100000:
    record = f.readline()
    if record == "":
        print("End of file")
        f.close()
        quit()

    # Working out the number of characters across each row to put the data into columns
    petallength = (record[0:3])
    petalwidth = (record[4:7])
    sepallength = (record[8:11])
    sepalwidth = (record[12:15])
    name = (record[16:30])

    print(petallength, petalwidth, sepallength, sepalwidth)
    record = ""
    c = c + 1