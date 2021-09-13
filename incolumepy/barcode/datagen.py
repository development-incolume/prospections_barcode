#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
from faker import Faker
from pathlib import Path
from random import sample, choices
import json


products_list = ['arroz', 'feijão', 'açúcar', 'café', 'macarrão', 'sal', 'azeite']
products = {x: ''.join(str(a) for a in choices(range(10), k=12)) for x in products_list}
fproduct = Path(__file__).parent/'products.json'

try:
    with open(fproduct, 'x') as f:
        json.dump(products, f, indent=4)
except FileExistsError as e:
    print(e)
