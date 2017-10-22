import datetime
date = datetime.date.today()
delta = datetime.timedelta(days=1, hours=16, minutes=48, seconds=55)
print(date)
print(delta)

class Date_iterator():
    def __init__(self, date, datedelta):
        self.iter_date = date
        self.iter_delta = datedelta
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == 10:
            raise StopIteration

        if self.i < 10:
            self.iter_date += self.iter_delta
            self.i += 1
            return(str(self.iter_date))

xz = Date_iterator(439000,5)
xzz = Date_iterator(date,delta)
for x in xz:
    print(x)
print()
for y in xzz:
    print(y)