class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity     
        self.size = 0
        
    
    def __str__(self):
        #return a cookie emoji 🍪 as str with n cokkies in the jar
        return f"🍪" * self._size
    
    def deposit(self, n):

        #raise value error if jar is full
        if self._size + n > self._capacity:
            raise ValueError("Jar is full")
        #add n cookies to the jar
        self.size += n

    def withdraw(self, n):
        #raise value error for insufficient cookies
        if self._size - n < 0:
            raise ValueError("Jar doesn't have enough cookies")
        #remove n cookies from the jar
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity <1:
            raise ValueError("Capacity must be a positive integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size must be less than capacity")
        self._size = size


def main():
    jar = Jar()
    jar.deposit(10)
    print(jar)



if __name__ == "__main__":
    main()