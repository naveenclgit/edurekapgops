class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Incorrect Value')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * '🍪'

    def deposit(self, n):
        if n > self._capacity or self._size + n > self._capacity:
            raise ValueError('Incorrect Value')
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError('Incorrect Value')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
print(str(jar.capacity))
jar.deposit(1)
print(jar)
jar.withdraw(1)
print(jar)
print(str(jar.size))
