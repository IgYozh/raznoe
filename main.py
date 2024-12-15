import inspect
from pprint import pprint

def introspection_info(obj):
    obj_type = type(obj).__name__ # Определяем тип объекта
    attributes = dir(obj) # Получаем его атрибуты
    methods = [method for method in attributes if callable(getattr(obj, method))] # Получем его методы
    module = obj.__class__.__module__ # Определяем модуль, к которому принадлежит объект
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},

    return info

# Проводим интроспекцию числа
number_info = introspection_info(59)
pprint(number_info)

# Проводим интроспекцию строки
string_info = introspection_info('JoJo-San')
pprint(string_info)

# Проводим интроспекцию списка
list_info = introspection_info([1, 20, 4.0, 'bulka'])
pprint(list_info)