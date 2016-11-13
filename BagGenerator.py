import time


class BagEntry:
    word = ""
    count = 1


def millis():
    return int(round(time.time() * 1000))


def parse_word(word):
    newword = ''.join(e for e in word if e.isalnum() and not e.isdigit())
    if len(newword) < 2:
        return ""
    return word


def update_bag(bag, word):
    newword = parse_word(word)
    if newword == "":
        return
    for b in bag:
        if b.word == newword:
            b.count += 1
            return
    n = BagEntry()
    n.word = newword
    bag.append(n)


def print_bag(bag):
    for b in bag:
        print "" + b.word + "\t" + str(b.count) + "\n"


def print_top_bag_words(bag, i=10):
    for j in range(i):
        print "" + bag[j].word + "\t" + str(bag[j].count) + "\n"


def save_bag_into_file(bag, filename):
    f = open(".\\" + filename, "w")
    sorted_bag = sorted(bag, key=lambda word: word.count, reverse=True)
    for b in sorted_bag:
        f.write(b.word + "\t" + str(b.count) + "\n")


def parse_file(bag_of_words, f):
    print "Reading from file " + f.name + " started."
    loops = 0
    t1 = millis()
    #for i in range(0, 1000):
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
        for s in splited2:
            update_bag(bag_of_words, s)
        loops += 1
        if loops % 10000 == 0:
            print str(loops) + " Time from start:" + str(millis() - t1)
    t2 = millis() - t1
    print "Reading from file " + f.name + " end. Time in ms: " + str(t2)


def main():
    file_name_format = 'D:\Magisterka\semestr2\callenge\\training.v2\\training.00{}.tsv'
    file_names = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]

    bag_of_words = []
    # for name in file_names[0:3]:
    for name in file_names:
        f = open(str.format(file_name_format, name), 'r')
        parse_file(bag_of_words, f)
        f.close()
    print_top_bag_words(sorted(bag_of_words, key=lambda word: word.count, reverse=True))
    save_bag_into_file(bag_of_words, "bag01")

    bag_of_words.sort()


if __name__ == "__main__":
    main()
