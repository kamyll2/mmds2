import time

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.svm import SVC
import math


def millis():
    return int(round(time.time() * 1000))


def save_solution_into_file(container, filename):
    f = open(".\\" + filename, "w")
    for key, value in container.iteritems():
        f.write(str(key) + "\t" + str(value) + "\n")


def read_test_file(f):
    print "Reading from file " + f.name + " started."
    loops = 0
    Ids = []
    t1 = millis()
    # for i in range(0, 1000):
    while True:
        line = f.readline()
        if line == "":
            break
        splited = line.split('\t')
        Ids.append(int(splited[0]))
        loops += 1
        if loops % 10000 == 0:
            print str(loops) + " Time from start:" + str(millis() - t1)
    t2 = millis() - t1
    print "Reading from file " + f.name + " end. Time in ms: " + str(t2)
    return Ids


def read_data_file(f, container):
    print "Reading from file " + f.name + " started."
    loops = 0
    t1 = millis()
    # for i in range(0, 1000):
    while True:
        line = f.readline()
        if line == "":
            break
        splited = line.split('\t')
        container[int(splited[0])] = int(splited[1])
        loops += 1
        if loops % 10000 == 0:
            print str(loops) + " Time from start:" + str(millis() - t1)
    t2 = millis() - t1
    print "Reading from file " + f.name + " end. Time in ms: " + str(t2)


def main():
    file_name_format = 'D:\Magisterka\semestr2\callenge\\training.v2\\training.00{}.tsv'
    file_names = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]

    IdsAll = []
    for name in file_names:
        file_name = str.format(file_name_format, name)
        f = open(file_name, 'r')
        Ids = read_test_file(f)
        IdsAll += Ids

        f.close()

    allResults = {}
    file_names = ["testSolution03", "testSolution36", "testSolution69", "testSolution99"]
    for name in file_names:
        f = open(name, 'r')
        read_data_file(f, allResults)
        f.close()

    for uniqueId in IdsAll:
        if uniqueId not in allResults:
            allResults[uniqueId] = 0

    print('END: \n')
    save_solution_into_file(allResults, "Solution")


if __name__ == "__main__":
    main()
