__author__ = "@britodfbr"
from pathlib import Path
from random import choices
from typing import List
import json
import logging


def datagen(products_list: List[str]):
    products_list = products_list or ['arroz', 'feijão', 'açúcar', 'café', 'macarrão', 'sal', 'azeite', 'chocolate']
    products = {x: ''.join(str(a) for a in choices(range(10), k=12)) for x in products_list}
    fproduct = Path(__file__).parent/'products.json'

    try:
        with open(fproduct, 'x') as f:
            json.dump(products, f, indent=2)
        return fproduct

    except FileExistsError as e:
        logging.error(e)
