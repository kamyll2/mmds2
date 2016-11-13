import time


class PairCategoryRank(object):
    def __init__(self, i, j):
        self.cat_map = {}
        self.i = i
        self.j = j

    i = -1
    j = -1
    cat_map = None
    count = 0

    def add_category(self, category):
        cnt = self.cat_map.get(category, -1)
        if cnt == -1:
            self.cat_map[category] = 1
        else:
            self.cat_map[category] = cnt + 1

    def to_str(self):
        string = "" + str(self.i) + ":" + str(self.j) + "\tcnt:" + str(self.count)
        for key in self.cat_map.keys():
            string += "\t" + str(key) + ":" + str(self.cat_map[key])
        return string


def millis():
    return int(round(time.time() * 1000))


def save_result_into_file(results, name):
    f = open(".\\out\\" + name, "w")
    for i in range(0, 100):
        for j in range(i + 1, 100):
            f.write(results[i][j].to_str() + "\n")
    f.close()


def parse_file(results, f):
    print "Reading from file " + f.name + " started."
    loops = 0
    t1 = millis()
    #for i in range(0, 100):
    while True:
        line = f.readline()
        if line == "":
            break
        line = line.replace('\n', '')
        splited = line.split('\t')
        categories = splited[101:]
        for k in range(1, 101):
            for l in range(k + 1, 101):
                if splited[k] == "1" and splited[l] == "1":
                    results[k - 1][l - 1].count += 1
                    for cat in categories:
                        results[k - 1][l - 1].add_category(cat)
        loops += 1
        if loops % 10000 == 0:
            print str(loops) + " Time from start:" + str(millis() - t1)
    t2 = millis() - t1
    print "Reading from file " + f.name + " end. Time in ms: " + str(t2)
    # save_result_into_file(results, name)


def main():
    file_name_format = '.\\out\\{}'
    file_names = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]

    # results = []
    # for i in range(0, 100):
    # results.append(CategoryRank())
    results = [None for k in range(100)]
    for i in range(0, 100):
        row = [None for k in range(100)]
        for j in range(i + 1, 100):
            row[j] = PairCategoryRank(i, j)
        results[i] = row

    # for name in file_names[0:3]:
    for name in file_names:
        f = open(str.format(file_name_format, name), 'r')
        parse_file(results, f)
        f.close()
    save_result_into_file(results, "pair_cat_groups")


if __name__ == "__main__":
    main()
