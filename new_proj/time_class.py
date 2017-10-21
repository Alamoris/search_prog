import datetime
date = datetime.date.today()
delta = datetime.timedelta(days=1, hours=16, minutes=48, seconds=55)
print(date)
print(delta)

class Date_iterator():
    def __init__(self, date, datedelta):
        self.iter_date = str(date)
        self.iter_delta = str(datedelta)
        self.index = len(self.iter_date) + len(self.iter_delta) - 1
        self.k = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        if self.index < len(self.iter_date):
            self.index -= 1
            return self.iter_date[self.index]
        else:
            i = self.k
            self.k += 1
            self.index -= 1
            return self.iter_delta[i]

xz = Date_iterator(date,delta)
for x in xz:
    print(x,end='')