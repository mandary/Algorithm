import random
import pdb

def stableMatching(size):
    popSize = size + 1
    M = range(1, popSize)
    Mproposal = [0] * size
    Wrank = [0] * size
    Mpref = randomizedPref(popSize)
    Wpref = randomizedPref(popSize)
    stableMatch = {}
    while len(M) > 0:
        m = M[0]
        prefindex = Mproposal[m - 1]
        w = Mpref[m][prefindex]
        cm = stableMatch.get(w, 0)
        Mproposal[m - 1] += 1
        wpref = Wpref[w]
        if cm is 0:
            stableMatch[w] = m
            M.pop(0)
            Wrank[w - 1] = wpref.index(m)
        elif wpref.index(m) < wpref.index(cm):
            stableMatch[w] = m
            M.pop(0)
            M.append(cm)
            Wrank[w - 1] = wpref.index(m)
    print Mpref
    print Wpref
    # women are the keys, men are the values
    print stableMatch
    print "Mrank: ", sum(Mproposal)
    print "Wrank: ", sum(Wrank) + size

def randomizedPref(size):
    pref = {}
    for i in range(1, size):
        prefList = range(1, size)
        random.shuffle(prefList)
        pref[i] = prefList
    return pref

stableMatching(5)