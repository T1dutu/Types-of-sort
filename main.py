import random,time

class Sort:
    def __init__(self,lenght_array,max_value):
        self.lenght_array = lenght_array
        self.max_value = max_value
        self.main_array = []
        self.execution_time = 0.0

    def create_array(self):
        self.main_array = [random.randint(1,self.max_value) for _ in range(self.lenght_array)]
    
    def _start_timer(self):
        self._start_time = time.perf_counter()

    def _stop_timer(self):
        self.execution_time = time.perf_counter() - self._start_time

    def get_array(self):
        return self.main_array
    
    def get_execution_time(self):
        return self.execution_time

class Bubble_sort(Sort):
    def sorting(self):
        self._start_timer()
        n = len(self.main_array)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.main_array[j] > self.main_array[j + 1]:
                    self.main_array[j],self.main_array[j + 1] = self.main_array[j + 1], self.main_array[j]
        self._stop_timer()
        return self.main_array
    
array = Bubble_sort(10000, 10000)
array.create_array()

array.sorting()

print("Отсортированный массив:", array.get_array())
print("Время сортировки:", array.get_execution_time(), "сек")
    
