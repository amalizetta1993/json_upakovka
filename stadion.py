import pickle
import json

class Stadium:
    def __init__(self, name, capacity, field_size):
        self.name = name  # название стадиона
        self.capacity = capacity  # вместимость зрителей
        self.field_size = field_size  # размер поля
        self.is_open = False  # статус открытия
        
    def open_stadium(self):
        if self.is_open:
            print(f"{self.name}: Стадион уже открыт")
        else:
            self.is_open = True
            print(f"{self.name}: Стадион открыт для посещения")
            
    def get_info(self):
        return f"Стадион '{self.name}':\n" \
               f"Вместимость: {self.capacity}\n" \
               f"Размер поля: {self.field_size}\n" \
               f"Статус: {'открыт' if self.is_open else 'закрыт'}"


class MyPickler:
    def __init__(self, protocol=pickle.DEFAULT_PROTOCOL):

        if protocol < 0 or protocol > 5:
            self.protocol = pickle.DEFAULT_PROTOCOL
        elif protocol == 0:
            self.protocol = pickle.HIGHEST_PROTOCOL
        else:
            self.protocol = protocol

    def pickle_data(self, data):
        pickled_data = pickle.dumps(data, self.protocol)
        return pickled_data

    def pickle_file(self, filename, data: object):
        with open(filename, 'wb') as fp:
            pickle.dump(data, fp, self.protocol)
        return f'Произведен пиклинг в файле {filename}'


class MyUnpickler:

    @classmethod
    def unpickle_data(cls, pickled_data):
        unpickle_data = pickle.loads(pickled_data)
        return unpickle_data

    @classmethod
    def unpickle_file(cls, pickled_filename):
        try:
            with open(pickled_filename, 'rb') as fp:
                unpickle_data = pickle.load(fp)
        except FileExistsError:
            return 'Файл не найден'
        return unpickle_data
    
olympic = Stadium("Олимпийский", 45000, "105x68 м")    
    
my_pickler_5 = MyPickler(protocol=5)
my_pickler_5.pickle_file('stadiums', olympic)
mus = MyUnpickler.unpickle_file('stadiums')    

