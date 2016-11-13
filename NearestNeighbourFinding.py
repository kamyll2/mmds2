import time


class NeighbourModel(object):
    def __init__(self, row, jaccard):
        self.id = int(row[0])
        self.categories = row[101:]
        self.jaccard = jaccard

    id = -1
    jaccard = -1.0
    categories = []

    def to_str(self):
        string = "[" + str(self.id) + "," + str(self.jaccard) + ",["
        first = True
        for cat in self.categories:
            if first:
                first = False
            else:
                string += " "
            string += cat
        string += "]]"
        return string


class NearestNeighbourHolder(object):
    def __init__(self, row):
        self.row = row
        self.nearest_neighbours = []

    row = []
    nearest_neighbours = []

    def try_to_add_neighbour(self, neighbour):
        if len(self.nearest_neighbours) < 10:
            self.nearest_neighbours.append(neighbour)
            self.sort_neighbours()
            return True
        if neighbour.jaccard > self.nearest_neighbours[-1].jaccard:
            self.nearest_neighbours[-1] = neighbour
            self.sort_neighbours()
            return True
        else:
            return False

    def sort_neighbours(self):
        self.nearest_neighbours.sort(key=lambda word: word.jaccard, reverse=True)

    def calculate_jaccard(self, row):
        if self.row[0] == row[0]:
            return 0.0
        and_count = 0
        or_count = 0
        for i in range(1, 101):
            sum_norm = int(row[i]) + int(self.row[i])
            if sum_norm > 1:
                and_count += 1
                or_count += 1
            elif sum_norm > 0:
                or_count += 1
        if and_count == 0:
            return 0.0
        else:
            return float(and_count) / float(or_count)

    def calculate_jaccard2(self, row):
        if self.row[0] == row[0]:
            return 0.0
        and_count = 0
        or_count = 0
        for i in range(1, 101):
            w1 = row[i] == "1"
            w2 = self.row[i] == "1"
            if w1 and w2:
                and_count += 1
                or_count += 1
            elif w1 or w2:
                or_count += 1
        if and_count == 0:
            return 0.0
        else:
            return float(and_count) / float(or_count)

    def to_str(self):
        string = str(self.row[0]) + "\t["
        first = True
        for cat in self.row[101:]:
            if first:
                first = False
            else:
                string += ";"
            string += cat
        string += "]\t["
        first = True
        for neigh in self.nearest_neighbours:
            if first:
                first = False
            else:
                string += ";"
            string += neigh.to_str()
        string += "]"
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
        for res in results:
            jaccard = res.calculate_jaccard2(splited)
            if jaccard > 0:
                res.try_to_add_neighbour(NeighbourModel(splited, jaccard))
        loops += 1
        if loops % 1000 == 0:
            print str(loops) + " Time from start:" + str(millis() - t1)
    t2 = millis() - t1
    print "Reading from file " + f.name + " end. Time in ms: " + str(t2)
    # save_result_into_file(results, name)


def init_result_list():
    result = []
    f = open(".\\out\\01", 'r')
    for i in range(0, 1000):
        result.append(NearestNeighbourHolder(f.readline().replace('\n', '').split('\t')))
    f.close()
    return result


def main():
    file_name_format = '.\\out\\{}'
    file_names = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]

    # results = []
    # for i in range(0, 100):
    # results.append(CategoryRank())
    results = init_result_list()
    # for name in file_names[0:3]:
    for name in file_names:
        f = open(str.format(file_name_format, name), 'r')
        parse_file(results, f)
        f.close()
    save_result_into_file(results, "nearest_neighbours")


if __name__ == "__main__":
    main()
