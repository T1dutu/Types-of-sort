import random

class Sort:
    def __init__(self,lenght_array,max_value):
        self.lenght_array = lenght_array
        self.max_value = max_value
        self.main_array = []

    def create_array(self):
        self.main_array = [random.randint(1,self.max_value) for _ in range(self.lenght_array)]
    
    def get_info(self):
        return self.main_array

class Bubble_sort(Sort):
    def sorting(self):
        n = len(self.main_array)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.main_array[j] > self.main_array[j + 1]:
                    self.main_array[j],self.main_array[j + 1] = self.main_array[j + 1], self.main_array[j]
        return self.main_array
array = Bubble_sort(10,100)
array.create_array()
print(array.get_info())
array.sorting()
print(array.get_info())                
