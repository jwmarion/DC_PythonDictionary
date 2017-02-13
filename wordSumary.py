#ex4

def word_histogram(input):
    tdict = {}
    for word in input.split():
        if tdict.get(word) == None:
            tdict[word] = 1
        else:
            tdict[word] += 1
    return tdict



print word_histogram("to be or not to be")
