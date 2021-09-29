from math import log

def init_ngrams(filename):
    dic = {}
    with open(filename) as f:
        for line in f:
            key,count = line.split(' ') 
            dic[key] = int(count)
        # for line in file(file):
        print(dic)

# print(init_ngram('./frequency/english_bigrams.txt'))

def compute_ngram():
    pass

