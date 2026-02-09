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
    
first_array = Sort(50,1000)
first_array.create_array()
print(first_array.get_info())
        

