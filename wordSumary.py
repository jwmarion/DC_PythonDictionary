#ex4

def word_histogram(input):
    tdict = {}
    for word in input.split():
        if tdict.get(word) == None:
            tdict[word] = 1
        else:
            tdict[word] += 1
    return tdict



print word_histogram("James is a student at Digital Crafts. He is twenty nine. He needs more duplicate words in this paragraph. is is  nine more.")
