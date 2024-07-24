class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        self.size += n
        return self._size

    def withdraw(self, n):
        if n > self.size:
           raise ValueError("Value exceeds size!")
        self.size -= n
        return self._size

    @property
    def capacity(self):
      return self._capacity

    @capacity.setter
    def capacity(self, capacity=12):
      if capacity < 0:
          raise ValueError("Undefined Capacity!")
      else:
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if size > self.capacity:
          raise ValueError("the value is bigger than the capacity!")
        else:
          self._size = size
