import ctypes


class Array:
    def __init__(self, size):
        self._size = size
        self._elements = ctypes.py_object*size
        self._array = self._elements()
        self._cntr = 0
        self.clear(None)

    def display(self):
        for i in range(self._size):
            print(self._array[i], end=' ')
        print('')

    def clear(self, value):
        for i in range(self._size):
            self._array[i] = value

    def __len__(self):
        return self._size

    def __getitem__(self, ndx):
        assert ndx >= 0 and ndx < self._size, "Index out of bound"
        return self._array[ndx]

    def __setitem__(self, ndx, item):
        assert ndx >= 0 and ndx < self._size, "Index out of bound"
        self._array[ndx] = item

    def __iter__(self):
        return self

    def __next__(self):
        if self._cntr < self._size:
            tmp = self._array[self._cntr]
            self._cntr += 1
            return tmp
        else:
            raise StopIteration


class Array2D:
    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def clear(self, value):
        for row in range(self.numRows()):
            self._theRows[row].clear(value)

    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(),\
            "Array subscript out of range"
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid no of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value


def setvalues(x):
    for i in range(x.numRows()):
        print('')
        for j in range(x.numCols()):
            x[i, j] = int(input('enter value %d,%d = ' % (i, j)))


def display(x):
    print('Your 2D-Array is here:')
    for i in range(x.numRows()):
        print('')
        for j in range(x.numCols()):
            print(x[i, j], end=" ")


twoDArray = Array2D(3, 3)
twoDArray.clear(0)
