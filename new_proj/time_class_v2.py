import datetime
date = datetime.date.today()
delta = datetime.timedelta(days=1, hours=16, minutes=48, seconds=55)
print(date)
print(delta)

class Date_iterator():
    def __init__(self, date, datedelta):
        self.iter_date = str(date)
        self.iter_delta = str(datedelta)
        self.index = len(self.iter_date) + len(self.iter_delta)
        self.k, self.j = 0, 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        if self.index <= len(self.iter_delta):
            i = self.k
            self.k += 1
            self.index -= 1
            return self.iter_delta[i]
        else:
            i = self.j
            self.j += 1
            self.index -= 1
            return self.iter_date[i]

xz = Date_iterator(4392528,2358235743)
xzz = Date_iterator(date,delta)
for x in xz:
    print(x,end='')
print()
for y in xzz:
    print(y, end='')