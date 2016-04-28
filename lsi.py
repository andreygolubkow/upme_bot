from scipy import linalg,sqrt
import numpy
class LSI(object):
    def __init__(self, stopwords, ignorechars, docs):
        self.docs=[]
        self.wdict = {}
        self.dictionary = []
        self.stopwords = stopwords
        if type(ignorechars) == unicode:
            ignorechars = ignorechars.encode('utf-8')
            self.ignorechars = ignorechars
        for doc in docs: self.add_doc(doc)
    def prepare(self):
        self.build()
        self.calc()
    def dic(self, word, add = False):
        if type(word) == unicode:
            word = word.encode('utf-8')
            word = word.lower().translate(None, self.ignorechars)
            word = word.decode('utf-8')
            word = stemmer.stemWord(word)
        if word in self.dictionary:
            return self.dictionary.index(word)
        else:
            if add:
                self.dictionary.append(word)
                return len(self.dictionary) - 1
            else: return None
    def add_doc(self, doc):
        words = [self.dic(word, True) for word in doc.lower().split()]
        self.docs.append(words)
        for word in words:
            if word in self.stopwords:
                continue
            elif word in self.wdict:
                self.wdict[word].append(len(self.docs) - 1)
            else:
                self.wdict[word] = [len(self.docs) - 1]
    def build(self):
        self.keys = [k for k in self.wdict.keys() if len(self.wdict[k]) > 0]
        self.keys.sort()
        self.A = numpy.zeros([len(self.keys), len(self.docs)])
        for i, k in enumerate(self.keys):
            for d in self.wdict[k]:
                self.A[i,d] += 1
    def calc(self):
        self.U, self.S, self.Vt = linalg.svd(self.A)
    def TFIDF(self):
        wordsPerDoc = sum(self.A, axis=0)
        docsPerWord = sum(asarray(self.A > 0, 'i'), axis=1)
        rows, cols = self.A.shape
        for i in range(rows):
            for j in range(cols):
                self.A[i,j] = (self.A[i,j] / wordsPerDoc[j]) * log(float(cols) / docsPerWord[i])
    def dump_src(self):
        self.prepare()
        print 'rasschet matr '
        for i, row in enumerate(self.A):
            print self.dictionary[i], row
    def print_svd(self):
        self.prepare()
        print 'ingular value'
        print self.S
        print 'u matr '
        for i, row in enumerate(self.U):
            print self.dictionary[self.keys[i]], row[0:3]
        print 'vt matr'
        print -1*self.Vt[0:3, :]
    def find(self, word):
        self.prepare()
        idx = self.dic(word)
        if not idx:
            print 'slovo nevstr'
            return []
        if not idx in self.keys:
            print 'stopword'
            return []
        idx = self.keys.index(idx)
        print 'word --- ', word, '=', self.dictionary[self.keys[idx]], '.\n'
        # ???????? ?????????? ?????
        wx, wy = (-1 * self.U[:, 1:3])[idx]
        print 'word {}\t{:0.2f}\t{:0.2f}\t{}\n'.format(idx, wx, wy, word)
        arts = []
        xx, yy = -1 * self.Vt[1:3, :]
        for k, v in enumerate(self.docs):
            ax, ay = xx[k], yy[k]
            dx, dy = float(wx - ax), float(wy - ay)
            arts.append((k, v, ax, ay, sqrt(dx * dx + dy * dy)))
        return sorted(arts, key = lambda a: a[4])                
