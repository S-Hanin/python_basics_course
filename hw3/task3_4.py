# -*- coding:utf8 -*-

# На вход функции передается строка с xml документом
# (тэги без аттрибутов, корневой элемент только один).
# Нужно выполнить следующее преобразование и
# вывести максимальную вложенность.
#    Пример:
#         a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
#         foo(a) ->
#         {
#             'name': 'root',
#             'children': [
#                 {'name': 'element1', 'children': []},
#                 {'name': 'element2', 'children': []},
#                 {
#                     'name': 'element3',
#                     'children': [
#                         {'name': 'element4', 'children': []}
#                     ]
#                 }
#             ]
#         }, 2
#       в данном случае у element4 тэга вложенность/глубина 2


import xml.etree.ElementTree as Et


def xm_to_dict(xml_string):
    def build(element: Et.Element):
        node = {'name': element.tag, 'children': []}
        for item in element:
            node['children'].append(build(item))
        if len(element) > 0:
            build.levels += 1
        return node

    doc = Et.fromstring(xml_string)
    build.levels = 0
    return build(doc), build.levels
