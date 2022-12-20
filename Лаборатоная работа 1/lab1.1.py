'''
1.Придумать и написать 3 абстрактных класса, описывающих любой объект.
Каждый класс следует оформлять в отдельном модуле.
Например, в качестве объектов могут выступать материальные сущности стол, дерево, и даже нематериальные стек, Facebook.
2.Для каждого класса выделить 2-3 характеристики и записать их в виде атрибутов.
Если на аргументы конструктора накладываются какие-то ограничения, которые в реальной жизни не допустимы,
то следует описать валидацию (проверку) этих аргументов.
3.Сформировать для каждого класса 2-3 метода, которые будет описывать возможные действия с объектом.
Реализацию самих методов писать не нужно, достаточно только названия.
Если на аргументы накладываются какие-то ограничения, которые в реальной жизни не допустимы,
то следует описать валидацию (проверку) этих аргументов.
4.Каждый метод должен содержать документацию с описанием аргументов(если они есть) и возвращаемого результата(если он есть).
5.Все аргументы методов и возвращаемые результаты должны содержать аннотацию типов.
6.В документации должен содержаться как минимум один doctest пример как пользоваться методом.
7.Результат представить в виде ссылки на репозиторий GitHub, а ещё предпочтительнее в виде Pull Request без указания reviewer.
'''


# TODO Написать 3 класса с документацией и аннотацией типов
class Kitty:
    """
    Создание и подготовка к работе объекта "Котик"

    :param age: Возраст кота
    :param fur_colour: Цвет шерсти кота
    :param name: Кличка кота

    Примеры:
    >>> cat = Kitty(2, 'black', 'mazik') # инициализация экемпляра класса
    """

    def __init__(self, age: int, fur_colour: str, name: str):
        if not isinstance(age, int):
            raise TypeError("Возраст котика - это число!")
        if age <= 0:
            raise ValueError("Возраст котика не может быть отрицательным!")
        self.age = age

        if not isinstance(fur_colour, str):
            raise TypeError("Цвет шерсти должен быть словом!")
        self.fur_colour = fur_colour

        if not isinstance(name, str):
            raise TypeError("Кличка котика - это слово!")
        if name.isdigit():
            raise ValueError("Никаких цифр в имени!")
        self.name = name

    def is_cute(self) -> bool:
        """
        Функция, которая проверяет является ли котик милым

        :return: Является ли кот милым

        Примеры:
        >>> cat = Kitty(2, 'black', 'mazik') # инициализация экемпляра класса
        >>> cat.is_cute()

        """
        ...

    def meows(self, can_meow: bool) -> bool:
        """
        Кот мяукает

        :param can_meow: умение кота мяукать (не все коты умеют)

        :raise TypeError: Если ответ не true или false, то вызываем ошибку

        :return: Мяукает ли кот

        Примеры:
        >>> cat = Kitty(2, 'black', 'mazik') # инициализация экемпляра класса
        >>> cat.meows(True)
        True
        """
        if not isinstance(can_meow, bool):
            raise TypeError('Надо ответить True или False')
        return can_meow


class Steel:
    """
    Создание и подготовка к работе объекта "Сталь"

    :param amount_of_carbon: Количество углерода в стали
    :param melting_temperature: Температура плавления стали

    :raise ValueError: Если количество углерода меньше или равно 0, то возвращается ошибка.
    :raise ValueError: Если температура плавления не входит в диапазон 1300-2000, то возвращается ошибка.

    Примеры:
    >>> basic_steel = Steel(0.26, 1508) # инициализация экемпляра класса
    """
    def __init__(self, amount_of_carbon: float, melting_temperature: int):
        if not isinstance(amount_of_carbon, float):
            raise TypeError("Количество углерода - это float")
        if amount_of_carbon <= 0:
            raise ValueError("Углерод в стали не может быть меньше или равен 0")
        self.amount_of_carbon = amount_of_carbon

        if not isinstance(melting_temperature, int):
            raise TypeError('Температура плавления - это целое число')
        if not 1300 <= melting_temperature <= 2000:
            raise ValueError('Температура плавления может быть в диапазоне 1300-2000')
        self.melting_temperature = melting_temperature

    def add_alloy(self, amount_of_alloy: float) -> None:
        """
        Функция, которая добавляет примеси

        :param amount_of_alloy: Количество добавляемой примеси

        :raise TypeError: Если ответ не float, то вызываем ошибку

        Примеры:
        >>> basic_steel = Steel(0.26, 1508)
        >>> basic_steel.add_alloy(12.564)
        """
        if not isinstance(amount_of_alloy, float):
            raise TypeError('Количество примеси может быть только float')
        ...

    def heating_treatment(self, method: str) -> None:
        """
        Способ термообработки стали.

        :param method: Метод термообработки
        :raise TypeError: Если метод термообработки не является типом str, то вызываем ошибку

        """
        if not isinstance(method, str):
            raise TypeError('Метод термообработки может быть только типа str')
        ...


class Developer():
    """
    Создание и подготовка к работе объекта "Разработчик"

    :param experience: Опыт работы в годах
    :param dev_language: Язык программирования разработчика

    Примеры:
    >>> ivan = Developer(3, 'Go') # инициализация экемпляра класса
    """

    def __init__(self, experience: int, dev_language: str):
        if not isinstance(experience, int):
            raise TypeError("Опыт может быть только int или float ")
        if experience <= 0:
            raise ValueError("Опыт работы не может быть меньше или равен 0")
        self.experience = experience

        if not isinstance(dev_language, str):
            raise TypeError("Язык программирования может быть только str")
        if dev_language.isdigit():
            raise ValueError("Это что за язык такой?")
        self.dev_language = dev_language

    def tired_of_work(self, work_after_six: bool) -> bool:
        """
        Функция, которая проверяет, устал ли разработчик от работы

        :param work_after_six: Работает ли разраб после 6

        :raise TypeError: Если ответ не true или false, то вызываем ошибку

        :return: Является ли разработчик уставшим/выгоревшим

        Примеры:
        >>> ivan = Developer(3, 'Go') # инициализация экемпляра класса
        >>> ivan.tired_of_work(True)
        True
        """
        if not isinstance(work_after_six, bool):
            raise TypeError('Надо ответить True или False')
        return work_after_six

    def hire(self) -> bool:
        """
        Функция, решающая нанять ли разработчика

        :return: Нанимать разработчика или нет

        Примеры:
        >>> ivan = Developer(3, 'Go') # инициализация экемпляра класса
        >>> ivan.hire()
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    pass
    doctest.testmod()
