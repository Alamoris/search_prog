class Exclamator():
    """Exclamate simbols"""
    def __init__(self, data):
        self.data = data
        self.index = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        self.index = self.index + 1
        return str(self.data[self.index]) + '!'

exc = Exclamator('spam')
iter(exc)
for char in exc:
    print(char)

