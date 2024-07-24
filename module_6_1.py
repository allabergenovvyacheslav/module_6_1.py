# Задача "Съедобное, несъедобное":

# Примечания:
# Помните, обращаясь к атрибутам объекта текущего класса используйте параметр self.
# Передавая объекты классов Fruit и Flower в метод eat, так же можно обращаться к их атрибутам внутри.
# Обращайте внимание на то, где атрибут класса, а где атрибут объекта.

# Создайте:
# 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное
# название каждого животного.
class Animal:
    def __init__(self, name):

        self.alive = True
        self.fed = False
        self.name = name

    # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
    # меняется атрибут fed на True.
    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        # Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
        # меняется атрибут alive на False.
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
class Plant:
    def __init__(self, name):
        self.edible = False # несъедобный
        self.name = name


class Mammal(Animal):  # Наследует атрибуты и методы из класса родителя
    pass


class Predator(Animal):  # Наследует атрибуты и методы из класса родителя
    pass


class Flower(Plant):  # Наследует атрибуты и методы из класса родителя
    pass


class Fruit(Plant):  # У каждого объекта Fruit должен быть атрибут
    # edible = True (переопределить при наследовании)
    def __init__(self, name):
        self.edible = True  # съедобный
        self.name = name


if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.