import dataclasses
import typing


def dict_to_dataclass(cls, values: typing.Dict):
    dataclass_items = {}
    cls_fields = [f.name for f in dataclasses.fields(cls)]
    for key, values in values.items():
        if key not in cls_fields:
            continue
        dataclass_items[key] = values

    return cls(**dataclass_items)