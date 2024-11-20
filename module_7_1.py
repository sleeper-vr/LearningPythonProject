

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return file.read()

    def add(self, *products):
        products_list = self.get_products().splitlines()
        for product in products:
            if product.name not in [p.split(',')[0] for p in products_list]:
                with open(self.__file_name, '+a', encoding='utf-8') as file:
                    file.write(f'{product.name}, {product.weight}, {product.category}\n')
            else:
                print(f'Продукт {product} уже есть в магазине')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
