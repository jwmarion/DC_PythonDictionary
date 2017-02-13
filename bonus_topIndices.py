#ex5
import operator

def word_histogram(input):
    tdict = {}
    for word in input.split():
        if tdict.get(word) == None:
            tdict[word] = 1
        else:
            tdict[word] += 1
    udict = sorted(tdict.items(), key=operator.itemgetter(1))
    z=len(udict)
    print "%s, %s, %s" % (udict[z-1], udict[z-2], udict[z-3])


word_histogram("James is a student at Digital Crafts. He is twenty nine. He needs more duplicate words in this paragraph. is is  nine more more.")
