import operator

def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

st=input("please enter a string")
output=most_frequent(st)
desc=dict(sorted(output.items(),key=operator.itemgetter(1),reverse=True))
print (desc)
