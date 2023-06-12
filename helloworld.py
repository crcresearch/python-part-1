class Tester:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f'Hello {self.name}!')
    
    def __say_goodbye(self):
        print(f'Goodbye {self.name}!')

    def bye(self):
        self.__say_goodbye()

import copy
a = Tester('John')
b = copy.deepcopy(a)

b.name = 'David'

a.say_hello()