from random import randint

def get_words_from_file(filename):
    content = []
    with open(filename, 'r') as f:
        content = [x.strip().split('\t') for x in f]
    return content

def retrieveThreeBestCategories(word):
    #print(word)
    temp = []
    categories = []
    for item in word:
        if('cnt' in item) :
            categories.append((int(item.replace('cnt:', ''))))
        else:
            temp.append(item.split(":"))
    unsorted_list = [[int(float(j)) for j in i] for i in temp]
    #print(unsorted_list)
    sortedList = sorted(unsorted_list, key = lambda x: int(x[1]))
    #print(sortedList)
    print(categories)

    category_1 = sortedList[len(sortedList) - 1]
    category_2 = sortedList[len(sortedList) - 2]
    category_3 = sortedList[len(sortedList) - 3]

    category_1[1] = category_1[1] / categories[0]
    category_2[1] = category_2[1] / categories[0]
    category_3[1] = category_3[1] / categories[0]

    print(category_1)
    print(category_2)
    print(category_3)

def retrieveThreeBestCategoriesPair(word):
    #print(word)
    temp = []
    categories = []
    pair = []
    pair.append(word[0])
    for item in word[1:]:
        if('cnt' in item) :
            categories.append((int(item.replace('cnt:', ''))))
        else:
            temp.append(item.split(":"))
    unsorted_list = [[int(float(j)) for j in i] for i in temp]
    #print(unsorted_list)
    sortedList = sorted(unsorted_list, key = lambda x: int(x[1]))
    #print(sortedList)
    print(pair)
    print(categories)

    category_1 = sortedList[len(sortedList) - 1]
    category_2 = sortedList[len(sortedList) - 2]
    category_3 = sortedList[len(sortedList) - 3]

    category_1[1] = category_1[1] / categories[0]
    category_2[1] = category_2[1] / categories[0]
    category_3[1] = category_3[1] / categories[0]

    print(category_1)
    print(category_2)
    print(category_3)


def main():

    words = get_words_from_file('out/pair_cat_groups')
    positions = [randint(0, 4949) for p in range(0, 5)]

    for position in positions:
        word = words[position]
        categories = retrieveThreeBestCategoriesPair(word)
        #print("Word position: " + position)
        #print(categories)
        #print("\n")



if __name__ == "__main__":
    main()
