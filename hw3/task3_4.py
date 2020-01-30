# -*- coding:utf8 -*-
import xml.etree.ElementTree as et


def xm_to_dict(xml_string):
    def build(element: et.Element, children: list):
        build.levels += 1
        for item in element:
            child = {'name': item.tag, 'children': []}
            children.append(child)
            if len(list(item)):
                build(item, child['children'])

    doc = et.fromstring(xml_string)
    tree = {'name': doc.tag, 'children': []}
    build.levels = 0
    build(doc, tree['children'])
    return tree, build.levels
