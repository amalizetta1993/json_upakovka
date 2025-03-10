class Book:
    def __init__(self, name, cost, availability):
        self.name = name
        self.cost = cost
        self.availability = availability
        
    def check_book(self):
        if self.availability:
            return print(f'Автомобиль перекрашен в {self.color} цвет')
    
    def sum_of_order(self, price, quantity):
        return print(f'Вы купили книгу {self.name} на сумму {self.price*self.quantity}')
        
            
car = Book('Преступление и наказание', '523 рубля', True)