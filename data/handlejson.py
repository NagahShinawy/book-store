"""
created by Nagaj at 05/05/2021
"""
import json
import os


class JsonMixin:
    PATH = ""
    OBJS = []

    @classmethod
    def load_objs(cls, objs_path):
        if not os.path.isfile(objs_path):
            return []
        with open(objs_path, "r") as f:
            data = json.load(f)
        return data

    @classmethod
    def save(cls, obj):
        if obj not in cls.OBJS:
            cls.OBJS.append(obj)

    @classmethod
    def to_json(cls):
        with open(cls.PATH, "w") as f:
            json.dump(cls.OBJS, f, indent=4)
