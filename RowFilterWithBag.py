import time


def millis():
    return int(round(time.time() * 1000))


def get_words_from_file(filename):
    f = open(".\\out\\" + filename, "r")
    words = []
    while True:
        line = f.readline()
        if line == "":
            break
        splited = line.split('\t')
        words.append(splited[0])
    f.close()
    return words


def update_norm(words, norm, s):
    for i in range(0, len(words)):
        if s.startswith(words[i]):
            norm[i] = 1
            break


def is_norm_empty(norm):
    for i in norm:
        if i == 1:
            return False
    return True


def add_result_row(results, splited, norm):
    row = []
    row.append(splited[0])
    row += norm
    row += splited[4:]
    results.append(row)


def save_result_into_file(results, name):
    f = open(".\\out\\" + name, "w")
    for row in results:
        for value in row:
            if value != row[0]:
                f.write('\t')
            f.write(str(value).replace('\n', ''))
        f.write('\n')
    f.close()


def parse_file(words, f, name):
    print "Reading from file " + f.name + " started."
    loops = 0
    t1 = millis()
    results = []
    #for i in range(0, 100):
    while True:
        line = f.readline()
        if line == "":
            break
        splited = line.split('\t')
        splited2 = splited[1].lower() \
            .replace('.', ' ') \
            .replace(',', ' ') \
            .replace('!', ' ') \
            .replace('-', ' ') \
            .replace('(', ' ') \
            .replace(')', ' ') \
            .split(' ')
        norm = [0] * 100  # fill by 0
        for s in splited2:
            update_norm(words, norm, s)
        if not is_norm_empty(norm):
            add_result_row(results, splited, norm)
        loops += 1
        if loops % 10000 == 0:
            print str(loops) + " Time from start:" + str(millis() - t1)
    t2 = millis() - t1
    print "Reading from file " + f.name + " end. Time in ms: " + str(t2)
    save_result_into_file(results, name)


def main():
    file_name_format = 'D:\Magisterka\semestr2\callenge\\training.v2\\training.00{}.tsv'
    file_names = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]

    words = get_words_from_file('bag_filtered.txt')
    # for name in file_names[0:3]:
    for name in file_names:
        f = open(str.format(file_name_format, name), 'r')
        parse_file(words, f, name)
        f.close()


if __name__ == "__main__":
    main()
