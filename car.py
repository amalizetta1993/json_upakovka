import pickle
import json

class Auto:
    def __init__(self, color, usage, age):
        self.color = color
        self.usage = usage
        self.age = age
        
    def change_color(self):
        self.color = input('В какой цвет вы хотите покрасить машину: ')
        return print(f'Автомобиль перекрашен в {self.color} цвет')
    
    def TO(self, use, ages):
        if use == 'личное':
            print('Техосмотр не нужен')
        else:
            print('Вам нужно пройти техосмотр')
            
        to_dict={
            '0':'нулевое ТО - 3000 рублей',
            '1':'нулевое ТО - 15300 рублей',
            '2':'нулевое ТО - 19020 рублей',
            '3':'нулевое ТО - 21000 рублей',
            '4':'нулевое ТО - 25900 рублей',                                                
        }
        if ages in to_dict:
            print(f'Вам нужно пройти {to_dict[ages]}')
        else:
            print('Обратитесь к консультанту для рассчета стоимости ТО')
            
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

car = Auto('белый', 'личное', '3')
    
my_pickler_5 = MyPickler(protocol=5)
my_pickler_5.pickle_file('cars', car)
mus = MyUnpickler.unpickle_file('cars')  
            
