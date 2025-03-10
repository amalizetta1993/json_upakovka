import pickle
import json

class Book:
    def __init__(self, name, cost, availability):
        self.name = name
        self.cost = cost
        self.availability = availability
        
    def check_book(self):
        if self.availability:
            return print(f'Книга {self.name} в наличии')
        else:
            return print('Книги в наличии нет')
    
    def change_cost(self):
        return print(f'Новая цена книги {self.name} - {self.price*1.05}')

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
    
book = Book('Преступление и наказание', '523 рубля', True)
    
my_pickler_5 = MyPickler(protocol=5)
my_pickler_5.pickle_file('books', book)
mus = MyUnpickler.unpickle_file('books')  
              
