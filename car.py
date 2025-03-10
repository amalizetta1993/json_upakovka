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
            
car = Auto('белый', 'личное', '3')