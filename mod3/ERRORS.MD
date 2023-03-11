## Ошибки
### Первая ошибка
    def get_age(self):
        now = datetime.datetime.now()
        return self.yob - now.year
#### Надо поменять self.yob и now.year местами, так как возвращается отрицательное число
    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.yob
<br/>

### Вторая ошибка
    def set_name(self, name):
        self.name = self.name

#### Надо полю класса присваивать не свое же поле, а переданный аргумент
    def set_name(self, name):
        self.name = name
<br/>

### Третья ошибка
    def set_address(self, address):
        self.address == address
#### Использованно сравнение, а не присваивание
    def set_address(self, address):
        self.address = address
<br/>

### Четвертая ошибка
    def is_homeless(self):
        '''
        returns True if address is not set, false in other case
        '''
        return address is None
#### Нужно обращаться к полю класса, а не к неинициализированной переменной, также self.adress никогда не будет None, потому что по дефолту стоит ''
    def is_homeless(self):
        '''
        returns True if address is not set, false in other case
        '''
        return self.address == ''