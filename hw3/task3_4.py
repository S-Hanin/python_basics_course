# -*- coding:utf8 -*-
import xml.etree.ElementTree as Et


def xm_to_dict(xml_string):
    def build(element: Et.Element, children: list):
        build.levels += 1
        for item in element:
            child = {'name': item.tag, 'children': []}
            children.append(child)
            if len(list(item)):
                build(item, child['children'])

    doc = Et.fromstring(xml_string)
    tree = {'name': doc.tag, 'children': []}
    build.levels = 0
    build(doc, tree['children'])
    return tree, build.levels
