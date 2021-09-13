#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"
import datagen
from barcode import EAN13
from barcode.writer import ImageWriter
import json
from pathlib import Path


def modo1():
    codigo_bar = EAN13("123123123123")
    codigo_bar.save('codigo_bar')


def modo2():
    codigo_bar = EAN13("123123123123", writer=ImageWriter())
    codigo_bar.save('codigo_bar')


def modo3(jsonfile=None, outputdir=None, png=False):
    jfile = jsonfile or Path(__file__).parent / 'products.json'
    writer = ImageWriter() if png else None
    outputdir = outputdir or Path(__file__).parent / 'barcodes'
    outputdir.mkdir(parents=True, exist_ok=True)

    with open(jfile) as f:
        products = json.load(f)
    # print(products)

    for product, code in products.items():
        print(product, code, end=' ')
        codigo_bar = EAN13(code, writer=writer)
        codigo_bar.save(outputdir/product)
        print('ok')


if __name__ == '__main__':
    # modo1()
    # modo2()
    # modo3()
    modo3(png=True)
