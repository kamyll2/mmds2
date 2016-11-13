import time


class CategoryRank(object):
    def __init__(self):
        self.cat_map = {}

    cat_map = None
    count = 0

    def add_category(self, category):
        cnt = self.cat_map.get(category, -1)
        if cnt == -1:
            self.cat_map[category] = 1
        else:
            self.cat_map[category] = cnt + 1

    def to_str(self):
        string = "cnt:" + str(self.count)
        for key in self.cat_map.keys():
            string += "\t" + str(key) + ":" + str(self.cat_map[key])
        return string


def millis():
    return int(round(time.time() * 1000))


def save_result_into_file(results, name):
    f = open(".\\out\\" + name, "w")
    for row in results:
        f.write(row.to_str() + "\n")
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
        for s in range(1, 101):
            if splited[s] == "1":
                results[s - 1].count += 1
                for cat in categories:
                    results[s - 1].add_category(cat)
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
    results = [CategoryRank() for i in range(100)]
    # for name in file_names[0:3]:
    for name in file_names:
        f = open(str.format(file_name_format, name), 'r')
        parse_file(results, f)
        f.close()
    save_result_into_file(results, "cat_groups")


if __name__ == "__main__":
    main()
