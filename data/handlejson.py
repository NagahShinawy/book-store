"""
created by Nagaj at 05/05/2021
"""
import json
import os


class JsonMixin:
    PATH = ""
    objs = []

    @classmethod
    def load_objs(cls, objs_path):
        if not os.path.isfile(objs_path):
            return []
        with open(objs_path, "r") as f:
            data = json.load(f)
        return data

    @classmethod
    def save(cls, obj):
        cls.objs.append(obj)

    @classmethod
    def to_json(cls):
        data = cls.remove_duplicates()
        with open(cls.PATH, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def remove_duplicates(cls):
        data = []
        for obj in cls.objs:
            if obj not in data:
                data.append(obj)
        return data
