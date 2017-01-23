import time
from sklearn.linear_model import LogisticRegression
from sklearn import tree
import math


def millis():
    return int(round(time.time() * 1000))


def read_file(f):
    print "Reading from file " + f.name + " started."
    loops = 0
    X = []
    Y1 = []
    Y2 = []
    Y3 = []
    t1 = millis()
    # for i in range(0, 1000):
    while True:
        line = f.readline()
        if line == "":
            break
        line = line.replace('\n', '')
        splited = line.split('\t')
        int_data = (map(int, splited))
        X.append(int_data[1:100])
        Y1.append(int_data[101])
        Y2.append(int_data[102])
        if len(int_data) > 103:
            Y3.append(int_data[103])
        else:
            Y3.append(-1)
        loops += 1
        if loops % 10000 == 0:
            print str(loops) + " Time from start:" + str(millis() - t1)
    t2 = millis() - t1
    print "Reading from file " + f.name + " end. Time in ms: " + str(t2)
    return X, Y1, Y2, Y3


def main():
    file_name_format = '.\\out\\{}'
    file_names = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]

    file_name = str.format(file_name_format, file_names[3])
    f = open(file_name, 'r')
    (X, Y1, Y2, Y3) = read_file(f)
    f.close()

    lines = len(X)
    train_range = int(math.floor(lines * 0.8))
    Y = Y1
    x_train = X[:train_range]
    x_test = X[train_range + 1:]
    y_train = Y[:train_range]
    y_test = Y[train_range + 1:]

    model = LogisticRegression(C=1)
    #model = tree.DecisionTreeClassifier(criterion='gini')
    # Train the model using the training sets and check score
    model.fit(x_train, y_train)
    model.score(x_train, y_train)
    # Equation coefficient and Intercept
    print('Coefficient: \n', model.coef_)
    #print('Intercept: \n', model.intercept_)
    # Predict Output
    predicted = model.predict_proba(x_test)

    hits = 0
    for i in range(0, len(y_test)):
        if y_test[i] == predicted[i]:
            hits += 1

    efficiency = float(hits) / len(y_test)
    print('EFFICIENCY: ', efficiency);
    print('END: \n')
    # for name in file_names[0:1]:
    # for name in file_names:
    # f = open(str.format(file_name_format, name), 'r')
    # parse_file(data, f)
    # f.close()
    # print_top_bag_words(sorted(data, key=lambda word: word.count, reverse=True))
    # save_bag_into_file(data, "bag01")


if __name__ == "__main__":
    main()
