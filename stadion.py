import pickle
import json

class Stadium:
    def __init__(self, name, capacity, is_open):
        self.name = name  # название стадиона
        self.capacity = capacity  # вместимость зрителей
        self.is_open = is_open  # статус открытия
        
    def __str__(self):
        return f"Stadium({self.name}, вместительность {self.capacity}, статус {self.is_open})"
        
    def open_stadium(self):
        if self.is_open:
            return f"{self.name}: Стадион уже открыт"
        else:
            return f"{self.name}: Стадион закрыт"
            
    def get_info(self):
        return f"Стадион '{self.name}':\n" \
               f"Вместимость: {self.capacity}\n" \
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
    
class JSONDataAdapter:
    
    @staticmethod
    def to_json(obj):
        if isinstance(obj, Stadium):
            return json.dumps({
                "Название": obj.name,
                "Вместимость": obj.capacity,
                "Статус": obj.is_open,
                "Открыт ли": obj.open_stadium()
            }, ensure_ascii=False )
                
    @staticmethod
    def from_json(json_str):     
        try: 
            obj = json.loads(json_str)
            stadion = Stadium(obj["Название"], obj["Вместимость"], obj["Статус"])
            return stadion
        except AttributeError:
            print('Неверная структура')
        
olympic = Stadium("Олимпийский", 45000, True)    
    
my_pickler_5 = MyPickler(protocol=5)
my_pickler_5.pickle_file('stadiums', olympic)
mus = MyUnpickler.unpickle_file('stadiums')    


json_1 = JSONDataAdapter.to_json(olympic)


print(json_1)

json_2 = JSONDataAdapter.from_json(json_1)

print(json_2)