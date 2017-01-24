import time

from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.svm import SVC
import math


def millis():
    return int(round(time.time() * 1000))


def save_solution_into_file(ids, predicted, filename):
    f = open(".\\" + filename, "w")
    for i in range(0, len(ids)):
        f.write(str(ids[i][0]) + "\t" + str(predicted[i]) + "\n")


def read_train_file(f):
    print "Reading from file " + f.name + " started."
    loops = 0
    Ids = []
    X = []
    Y1 = []
    Y2 = []
    t1 = millis()
    # for i in range(0, 1000):
    while True:
        line = f.readline()
        if line == "":
            break
        line = line.replace('\n', '')
        splited = line.split('\t')
        int_data = (map(int, splited))
        Ids.append(int_data[0:1])
        X.append(int_data[1:100])
        Y1.append(int_data[101])
        Y2.append(int_data[102])
        # if len(int_data) > 103:
        # Y3.append(int_data[103])
        # else:
        # Y3.append(-1)
        loops += 1
        if loops % 10000 == 0:
            print str(loops) + " Time from start:" + str(millis() - t1)
    t2 = millis() - t1
    print "Reading from file " + f.name + " end. Time in ms: " + str(t2)
    return Ids, X, Y1, Y2  # , Y3


def read_test_file(f):
    print "Reading from file " + f.name + " started."
    loops = 0
    Ids = []
    X = []
    t1 = millis()
    # for i in range(0, 1000):
    while True:
        line = f.readline()
        if line == "":
            break
        line = line.replace('\n', '')
        splited = line.split('\t')
        int_data = (map(int, splited))
        Ids.append(int_data[0:1])
        X.append(int_data[1:100])
        loops += 1
        if loops % 10000 == 0:
            print str(loops) + " Time from start:" + str(millis() - t1)
    t2 = millis() - t1
    print "Reading from file " + f.name + " end. Time in ms: " + str(t2)
    return Ids, X


def main():
    trainMode = False
    file_name_format = '.\\out\\test{}'
    file_names = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]

    # model = LogisticRegression(C=1)
    # model = SVC(C=10, kernel='linear')
    # model = RandomForestClassifier(n_jobs=4)
    IdsAll = []
    X_all = []
    Y1_all = []
    Y2_all = []
    for name in file_names[9:]:
        file_name = str.format(file_name_format, name)
        f = open(file_name, 'r')
        if trainMode:
            (Ids, X, Y1, Y2) = read_train_file(f)
            IdsAll += Ids
            X_all += X
            Y1_all += Y1
            Y2_all += Y2
        else:
            (Ids, X) = read_test_file(f)
            IdsAll += Ids
            X_all += X
        f.close()

    modelY1 = joblib.load('BaseRandomForestY1.pkl')
    modelY2 = joblib.load('BaseRandomForestY2.pkl')

    predicted_probaY1 = modelY1.predict_proba(X_all)
    predicted_probaY2 = modelY2.predict_proba(X_all)

    predictedY1 = []
    for p in predicted_probaY1:
        maxvar = max(p)
        idx = p.tolist().index(maxvar)
        clazz = modelY1.classes_[idx]
        predictedY1.append([clazz, maxvar])

    predictedY2 = []
    for p in predicted_probaY2:
        maxvar = max(p)
        idx = p.tolist().index(maxvar)
        clazz = modelY2.classes_[idx]
        predictedY2.append([clazz, maxvar])

    finalPredicted = []
    for i in range(0, len(predictedY1)):
        if predictedY2[i][1] > 0.5:
            finalPredicted.append(predictedY2[i][0])
        elif predictedY1[i][1] > 0.5:
            finalPredicted.append(predictedY1[i][0])
        else:
            finalPredicted.append(0)

    if trainMode:
        hits = 0
        nonzeros = 0
        for i in range(0, len(Y1_all)):
            if finalPredicted[i] == Y1_all[i] or finalPredicted[i] == Y2_all[i]:
                hits += 1
            if finalPredicted[i] != 0:
                nonzeros += 1

        efficiency = float(hits) / len(Y1_all)
        efficiency_non_zeros = float(hits) / nonzeros
        print('EFFICIENCY: ', efficiency)
        print('EFFICIENCY NON ZEROS: ', efficiency_non_zeros)

    print('END: \n')
    save_solution_into_file(IdsAll, finalPredicted, "testSolution99")


if __name__ == "__main__":
    main()
