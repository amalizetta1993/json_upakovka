import pickle
import json

class Book:
    def __init__(self, name, cost, availability):
        self.name = name
        self.cost = cost
        self.availability = availability
        
    def get_data(self):
        return self.name, self.cost, self.availability
        
    def check_availability(self):
        if self.availability:
            return f'Книга {self.name} в наличии'
        else:
            return 'Книги в наличии нет'
    
    def change_cost(self):
        return f'Новая цена книги {self.name} - {self.cost*1.05} рубля'
    

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

class MyBookEncoder(json.JSONEncoder):
    
    def default(self, o):
        return {
            "Название": o.name,
            "Стоимость": o.cost,
            "Наличие": o.availability,
            "Methods": {
                "Получение данных": o.get_data(),
                "Наличие": o.check_availability(),                
                "Изменение цены": o.change_cost()                   
            },
            "ClassName": o.__class__.__name__
        }
        
book = Book('Преступление и наказание', 523, True)
    
my_pickler_5 = MyPickler(protocol=5)
my_pickler_5.pickle_file('books', book)
mus = MyUnpickler.unpickle_file('books')  
              
# json_data = json.dumps(book, cls=MyBookEncoder, ensure_ascii=False, indent=2)      
# print(json_data)
# python_book_from_file = json.loads(json_data)
# print(python_book_from_file)

#json
with open(r'my_book_encode.json', 'w', encoding='utf-8') as fh:
       json.dump(book, fh, 
                 cls=MyBookEncoder,
                 ensure_ascii=False, indent=2)

with open(r'my_book_encode.json', 'r', encoding='utf-8') as fh:
       python_book_from_file = json.load(fh)
       
print(python_book_from_file)