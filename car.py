import pickle
import json

class Auto:
    def __init__(self, color, usage, age):
        self.color = color
        self.usage = usage
        self.age = age
    
    def get_data(self):
        return self.color, self.usage, self.age
        
    def change_color(self):
        self.color = input('В какой цвет вы хотите покрасить машину: ')
        return f'Автомобиль перекрашен в {self.color} цвет'
    
    def teh_osmotr(self):
        if self.usage == 'личное':
            teh = f'Техосмотр не нужен'
        else:
            teh = f'Вам нужно пройти техосмотр'
            
        to_dict={
            '0':'нулевое тех.обслуживание - 3000 рублей',
            '1':'нулевое тех.обслуживание - 15300 рублей',
            '2':'нулевое тех.обслуживание - 19020 рублей',
            '3':'нулевое тех.обслуживание - 21000 рублей',
            '4':'нулевое тех.обслуживание - 25900 рублей',                                                
        }
        if self.age in to_dict:
            teh_o = f'Вам нужно пройти {to_dict[self.age]}'
        else:
            teh_o = f'Обратитесь к консультанту для рассчета стоимости ТО'
        return f'{teh}. {teh_o}'  
     
    # @staticmethod
    # def to_json(obj):
    #     if isinstance(obj, Auto):
    #         result = obj.__dict__
    #         result['ClassName'] = obj.__class__.__name__
    #         result['Methods'] = ["Many Methods"]
    #         return result
    #     return None
            
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
    

        
class MyCarEncoder(json.JSONEncoder):
    
    def default(self, o):
        return {
            "Цвет": o.color,
            "Использование": o.usage,
            "Сколько лет машине": o.age,
            "Methods": {
                "Получение данных": o.get_data(),
                "Изменение цвета машины": o.change_color(),                
                "Необходимость техосмотра, цена техобслуживания": o.teh_osmotr()                   
            },
            "ClassName": o.__class__.__name__
        }

car = Auto('белый', 'личное', '3')
 
#пиклинг-распиклинг   
my_pickler_5 = MyPickler(protocol=5)
my_pickler_5.pickle_file('cars', car)
mus = MyUnpickler.unpickle_file('cars')  


# json_data = json.dumps(car, cls=MyCarEncoder, ensure_ascii=False, indent=2)      
# print(json_data)
# python_car_from_file = json.loads(json_data)
# print(python_car_from_file)

#json
with open(r'my_car_encode.json', 'w', encoding='utf-8') as fh:
       json.dump(car, fh, 
                 cls=MyCarEncoder,
                 ensure_ascii=False, indent=2)

with open(r'my_car_encode.json', 'r', encoding='utf-8') as fh:
       python_car_from_file = json.load(fh)
       
print(python_car_from_file)