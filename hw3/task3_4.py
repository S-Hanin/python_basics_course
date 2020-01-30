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
    def build(element: Et.Element, children: list):
        build.levels += 1
        for item in element:
            child = {'name': item.tag, 'children': []}
            children.append(child)
            if len(list(item)) > 0:
                build(item, child['children'])

    doc = Et.fromstring(xml_string)
    tree = {'name': doc.tag, 'children': []}
    build.levels = 0
    build(doc, tree['children'])
    return tree, build.levels
