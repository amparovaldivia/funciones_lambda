class Underscore:
    def map(self, iterable, callback):
        r = []
        for x in iterable:
            r.append(callback(x))
        return r
    def find(self, iterable, callback):
        for x in iterable:
            if callback(x)==True:
                return x
    def filter(self, iterable, callback):
        r=[]
        for x in iterable:
            if callback(x)==True:
                r.append(x)
        return r
    def reject(self, iterable, callback):
        r=[]
        for x in iterable:
            if callback(x)==False:
                r.append(x)
        return r

