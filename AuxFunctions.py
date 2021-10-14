def hamdist(str1, str2):
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                    diffs += 1
    return diffs
def searchclosest(x,mydict):

    mindist = 1000
    for key in mydict:
        dist = hamdist(x,key)
        if(dist < mindist):
            mindist = dist
            minentry = key
    return minentry