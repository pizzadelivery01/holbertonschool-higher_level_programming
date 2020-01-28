#!/usr/bin/python3
"""
contains "Base" class
"""

import json
import csv


class Base:
    """ Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json string of a list of dictionaries """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ list from json string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ json to obj file """
        filename = cls.__name__ + ".json"
        listo = []
        if list_objs is not None:
            for i in list_objs:
                listo.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(listo))

    @classmethod
    def create(cls, **dictionary):
        """ creates instance with attributes set """
        if cls.__name__ == 'Rectangle':
            temp = cls(1, 1)
        if cls.__name__ == 'Square':
            temp = cls(1)
        else:
            temp = None
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """ loading json from inside files """
        filename = cls.__name__ + ".json"
        li = []
        try:
            with open(filename, 'r') as f:
                li = cls.from_json_string(f.read())
            for i, obj in enumerate(li):
                li[i] = cls.create(**obj)
        except IOError:
            return []
        return li

    @classmethod
    def save_to_filecsv(cls, list_objs):
        """ makes into a list of Rectangles/Squares in csv format """
        filename = cls.__name__ + ".csv"
        li = []
        try:
            with open(filename, 'r') as filecsv:
                scanner = csv.reader(filecsv)
                for args in scanner:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    new = cls.create(**dictionary)
                    li.append(new)
        except:
            pass
        return li
