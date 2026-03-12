"""
Print numbers from 1 to N using two threads alternatively

"""

import threading

class AlternativePrinter:
    def __int__(self, n):
        self.n = n 
        self.num = 1
        self.lock = threading.Lock()
        self.turn = 1
    
    def print_odd(self):
        while self.num < self.n:
            with self.lock:
                if self.turn == 1 and self.num % 2 == 1:
                    print(f"Odd {self.num}")
                    self.num += 1
                    self.turn = 0
    
    def print_even(self):
        while self.num <= self.n:
            with self.lock:
                if self.turn == 0 and self.num % 2 == 0:
                    print(f"Even {self.num}")
                    self.num += 1
                    self.turn = 1

n = 100
printer = AlternativePrinter(n)
t1 = threading.Thread(target=printer.print_odd)
t2 = threading.Thread(target=printer.print_even)

t1.start()
t2.start()

t1.join()
t2.join()