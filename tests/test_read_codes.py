# -*- coding: utf-8 -*-

import os
from unittest import TestCase
from PIL import Image

from zxinglight import read_codes, BarcodeType


def get_image(name):
    file_path = os.path.join(os.path.dirname(__file__), 'fixtures', name + '.png')

    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()

    return image


class ReadCodesTestCase(TestCase):

    def test_no_qr_code(self):
        self.assertEqual(read_codes(get_image('no_qr_code')), [])

    def test_one_qr_code(self):
        image = get_image('one_qr_code')

        self.assertEqual(read_codes(image, barcode_type=BarcodeType.QR_CODE), [
            'zxinglight test qr code'
        ])

        self.assertEqual(read_codes(image, barcode_type=BarcodeType.CODE_39), [])

    def test_two_qr_code(self):
        self.assertEqual(sorted(read_codes(get_image('two_qr_codes'))), [
            'first zxinglight test qr code', 'second zxinglight test qr code'
        ])

    def test_small_rotated_qr_code(self):
        self.assertEqual(read_codes(get_image('small_rotated_qr_code'), try_harder=True), [
            '217EXP0112'
        ])
