import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

# 1. Геттеры и сеттеры
    @property
    def name_items(self):
        return self.__name_items
    
    @name_items.setter
    def name_items(self, value):
        self.__name_items = value
    
    @property
    def number_items(self):
        return self.__number_items
    
    @number_items.setter
    def number_items(self, value):
        self.__number_items = value
    
    @property
    def item_price(self):
        return self.__item_price
    
    @property
    def tax_rate(self):
        return self.__tax_rate
    
# 2. Добавить товар в чек    
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        
        self.name_items.append(name)
        self.number_items += 1

# 3. Удалить товар из чека 
    def delete_item_from_check(self, name):
        if name not in self.name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.name_items.remove(name)
            self.number_items -= 1


# 4. Посчитать общую стоимость товаров
    def check_amount(self):
        total = []
        for item in self.name_items:
            if item in self.item_price:
                total.append(self.item_price[item])
            else:
                raise ValueError(f"Цена для товара '{item}' не найдена в справочнике")
        
        sum_total = sum(total)
        
        if self.number_items > 10:
            sum_total * 0.9  # Скидка 10%
        return sum_total
    
# 5. Вычислить НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = [item for item in self.name_items 
                            if self.tax_rate.get(item) == 20]
            
        total = [self.item_price[item] for item in twenty_percent_tax]
        total_sum = sum(total) * 0.2

        if self.number_items > 10:
            total_sum *= 0.9
        return total_sum

# 6. Вычислить НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = [item for item in self.name_items 
                          if self.tax_rate.get(item) == 10]
            
        total = [self.item_price[item] for item in ten_percent_tax]
        total_sum = sum(total) * 0.1
        
        if self.number_items > 10:
            total_sum *= 0.9
        return total_sum

# 7. Посчитать общую сумму налогов
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
    
# 8. Вернуть номер телефона покупателя    
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        phone = f'+7{telephone_number}'
        return phone
    

# 9. Дополнительное задание. Возврат даты и времени покупки
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()

        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]

        for item in date:
            name, func = item[0], item[1]
            value = func(now)
            date_and_time.append(f'{name}: {value}')

        return date_and_time