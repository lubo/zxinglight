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
            b'zxinglight test qr code'
        ])

        self.assertEqual(read_codes(image, barcode_type=BarcodeType.CODE_39), [])

    def test_two_qr_code(self):
        self.assertEqual(sorted(read_codes(get_image('two_qr_codes'))), [
            b'first zxinglight test qr code', b'second zxinglight test qr code'
        ])

    def test_finding_one_of_two_qr_code(self):
        self.assertEqual(
            read_codes(get_image('two_qr_codes'), multi=False), [b'first zxinglight test qr code'],
        )

    def test_small_rotated_qr_code(self):
        self.assertEqual(
            read_codes(get_image('small_rotated_qr_code'), try_harder=True), [b'217EXP0112'],
        )

    def test_small_rotated_qr_code_single(self):
        self.assertEqual(
            read_codes(get_image('small_rotated_qr_code'), try_harder=True, multi=False),
            [b'217EXP0112'],
        )

    def test_embedded_nuls(self):
        """
        amen-*.png contain a music sample -- binary dara with anything goes including embedded nuls.

        They were created with
        cat amen.mp3 | qrencode -S -v 16 -8 -o amen.png  # -8 = bytes = binary
        """

        codes = read_codes(get_image('amen-02'), barcode_type=BarcodeType.QR_CODE,
                           try_harder=True, multi=False)
        self.assertTrue(len(codes) > 0)
        mp3_chunk = codes[0]
        print(mp3_chunk)
        self.assertTrue(b"\x00" in mp3_chunk)
