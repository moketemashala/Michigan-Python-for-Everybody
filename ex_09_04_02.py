fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
lst = list()
for lin in hand :
    if lin.startswith("From ") :
        lin = lin.rstrip()
        wds = lin.split()
        wds = wds[1]
        lst.append(wds)
print(lst)
for w in lst :
        #idiom: retrieve/create/update counter all in one
        di[w] = di.get(w,0) + 1
        #print(w, di[w])

#print(di)

#now we want to find the most common words
largest = -1  # for counters that are always greater than 0, then we can use -1
theword = None
for k,v in di.items() :
    #print(k,v)
    if v > largest :
        largest = v
        theword = k #capture/remember the key that was largest
print(theword, largest)
