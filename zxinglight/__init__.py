# -*- coding: utf-8 -*-

from enum import IntEnum, unique
try:
    from PIL import Image
except ImportError:
    pass
try:
    import cv2
    import numpy as np
except ImportError:
    pass

from ._zxinglight import zxing_read_codes


@unique
class BarcodeType(IntEnum):
    """
    Enumeration of barcode types supported by ZXing.
    """

    #: Default barcode type. If used, ZXing will read all types of barcodes.
    NONE = 0

    #:
    AZTEC = 1

    #:
    CODABAR = 2

    #:
    CODE_39 = 3

    #:
    CODE_93 = 4

    #:
    CODE_128 = 5

    #:
    DATA_MATRIX = 6

    #:
    EAN_8 = 7

    #:
    EAN_13 = 8

    #:
    ITF = 9

    #:
    MAXICODE = 10

    #:
    PDF_417 = 11

    #:
    QR_CODE = 12

    #:
    RSS_14 = 13

    #:
    RSS_EXPANDED = 14

    #:
    UPC_A = 15

    #:
    UPC_E = 16

    #:
    UPC_EAN_EXTENSION = 17


def read_codes_full(image, barcode_type=BarcodeType.NONE,
                    try_harder=False, hybrid=False, multi=True):
    """
    Reads codes from a PIL Image and includes metadata about what was found.

    Args:
        image (PIL.Image.Image): Image to read barcodes from.
        barcode_type (zxinglight.BarcodeType): Barcode type to look for.
        try_harder (bool): Spend more time trying to find a barcode.
        hybrid (bool): Use Hybrid Binarizer instead of Global Binarizer. For more information,
            see `ZXing's documentation`_.
        multi (bool): Search for multiple barcodes in a single image.

    Returns:
        A list [(code, position, type), ...] containing each barcode found.

    .. _ZXing's documentation:
        https://zxing.github.io/zxing/apidocs/com/google/zxing/Binarizer.html
    """

    if "Image" in globals() and Image.isImageType(image):
        grayscale_image = image.convert('L')

        raw_image = grayscale_image.tobytes()
        width, height = grayscale_image.size
    elif "cv2" in globals() and isinstance(image, np.ndarray):
        if image.dtype != np.uint8:
            raise TypeError("Provided cv2 image is not in integer bitdepth.")
        if len(image.shape) == 2:
            greyscale_image = image
        elif len(image.shape) == 3 and image.shape[-1] == 3:
            greyscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            raise TypeError("Provided cv2 image is not in BGR nor greyscale formats.")
        raw_image = greyscale_image.tobytes()
        height, width = image.shape[:2]
    else:
        raise TypeError('Provided image is not a PIL nor cv2 image')

    if not isinstance(barcode_type, BarcodeType):
        raise ValueError('barcode_type is not an enum member of BarcodeType')

    return zxing_read_codes(raw_image, width, height, barcode_type, try_harder, hybrid, multi)


def read_codes(*args, **kwargs):
    """
    Reads codes from a PIL Image.

    Args:
        image (PIL.Image.Image): Image to read barcodes from.
        barcode_type (zxinglight.BarcodeType): Barcode type to look for.
        try_harder (bool): Spend more time trying to find a barcode.
        hybrid (bool): Use Hybrid Binarizer instead of Global Binarizer. For more information,
            see `ZXing's documentation`_.
        multi (bool): Search for multiple barcodes in a single image.

    Returns:
        A list of barcode contents found.

    .. _ZXing's documentation:
        https://zxing.github.io/zxing/apidocs/com/google/zxing/Binarizer.html
    """
    codes = read_codes_full(*args, **kwargs)
    return [text for text, points, format in codes]
