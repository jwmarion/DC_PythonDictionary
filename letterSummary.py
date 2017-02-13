#ex3

def letter_histogram(word):
    tdict = {}
    for x in xrange(len(word)):
        if tdict.get(word[x]) == None:
            tdict[word[x]] = 1
        else:
             tdict[word[x]] += 1
    return tdict




print letter_histogram('Banana')
