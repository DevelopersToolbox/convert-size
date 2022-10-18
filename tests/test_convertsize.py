"""
Documentation to go here
"""

import pytest

from convertsize.convertsize import convert_size, convert_size_iec, convert_size_si, get_name_from_code, get_name_from_code_iec, get_name_from_code_si

tests = [
          {
            'IEC': {
                     'name': 'Byte',
                     'code': 'B',
                     'bytes': 1,
                   },
            'SI': {
                    'name': 'Byte',
                    'code': 'B',
                    'bytes': 1,
                  },
          },
          {
            'IEC': {
                     'name': 'Kibibyte',
                     'code': 'KiB',
                     'bytes': 1024,
                   },
            'SI': {
                    'name': 'kilobyte',
                    'code': 'KB',
                    'bytes': 1000,
                  },
          },
          {
            'IEC': {
                     'name': 'Mebibyte',
                     'code': 'MiB',
                     'bytes': 1048576,
                   },
            'SI': {
                    'name': 'Megabyte',
                    'code': 'MB',
                    'bytes': 1000000,
                  },
          },
          {
            'IEC': {
                     'name': 'Gibibyte',
                     'code': 'GiB',
                     'bytes': 1073741824,
                   },
            'SI': {
                    'name': 'Gigabyte',
                    'code': 'GB',
                    'bytes': 1000000000,
                  },
          },
          {
            'IEC': {
                     'name': 'Tebibyte',
                     'code': 'TiB',
                     'bytes': 1099511627776,
                   },
            'SI': {
                    'name': 'Terabyte',
                    'code': 'TB',
                    'bytes': 1000000000000,
                  },
          },
          {
            'IEC': {
                     'name': 'Pebibyte',
                     'code': 'PiB',
                     'bytes': 1125899906842624,
                   },
            'SI': {
                    'name': 'Petabyte',
                    'code': 'PB',
                    'bytes': 1000000000000000,
                  },
          },
          {
            'IEC': {
                     'name': 'Exbibyte',
                     'code': 'EiB',
                     'bytes': 1152921504606846976,
                   },
            'SI': {
                    'name': 'Exabyte',
                    'code': 'EB',
                    'bytes': 1000000000000000000,
                  },
          },
          {
            'IEC': {
                     'name': 'Zebibyte',
                     'code': 'ZiB',
                     'bytes': 1180591620717411303424,
                   },
            'SI': {
                    'name': 'Zettabyte',
                    'code': 'ZB',
                    'bytes': 1000000000000000000000,
                  },
          },
          {
            'IEC': {
                     'name': 'Yobibyte',
                     'code': 'YiB',
                     'bytes': 1208925819614629174706176,
                   },
            'SI': {
                    'name': 'Yottabyte',
                    'code': 'YB',
                    'bytes': 1000000000000000000000000,
                  },
          },
        ]

SIZE = 1


def test_zero():
    """
    Test 0 bytes password
    """
    assert convert_size(0, 'B', 'MiB') == 0  # nosec: B101


def test_zero_iec():
    """
    Test 0 bytes password
    """
    assert convert_size_iec(0, 'B', 'MiB') == 0  # nosec: B101


def test_zero_si():
    """
    Test 0 bytes password
    """
    assert convert_size_si(0, 'B', 'MiB') == 0  # nosec: B101


def test_get_name_from_code():
    """
    Test 0 bytes password
    """
    assert get_name_from_code('MiB') == 'Mebibyte'  # nosec: B101


def test_get_name_from_code_iec():
    """
    Test 0 bytes password
    """
    assert get_name_from_code_iec('MiB') == 'Mebibyte'  # nosec: B101


def test_get_name_from_code_si():
    """
    Test 0 bytes password
    """
    assert get_name_from_code_si('MB') == 'Megabyte'  # nosec: B101


def test_invalid_options():
    """
    Test passing invalid option
    """
    with pytest.raises(Exception):
        __unused = convert_size(SIZE, 'B', 'MB') == SIZE  # nosec: B101


def get_type(code, section = 'IEC'):
    """
    Docs to come
    """
    return next((item[section] for item in tests if item[section]["code"] == code), False)


def test_byte():
    """
    Docs to come
    """
    test = get_type('B', 'IEC')
    assert convert_size(SIZE, test['code'], 'B') == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code']) == SIZE  # nosec: B101


def test_byte_si():
    """
    Docs to come
    """
    test = get_type('B', 'SI')
    assert convert_size(SIZE, test['code'], 'B', True) == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code'], True) == SIZE  # nosec: B101


def test_kilobyte():
    """
    Docs to come
    """
    test = get_type('KiB', 'IEC')
    assert convert_size(SIZE, test['code'], 'B') == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code']) == SIZE  # nosec: B101


def test_kilobyte_si():
    """
    Docs to come
    """
    test = get_type('KB', 'SI')
    assert convert_size(SIZE, test['code'], 'B', True) == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code'], True) == SIZE  # nosec: B101


def test_megabyte():
    """
    Docs to come
    """
    test = get_type('MiB', 'IEC')
    assert convert_size(SIZE, test['code'], 'B') == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code']) == SIZE  # nosec: B101


def test_megabyte_si():
    """
    Docs to come
    """
    test = get_type('MB', 'SI')
    assert convert_size(SIZE, test['code'], 'B', True) == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code'], True) == SIZE  # nosec: B101


def test_gigabyte():
    """
    Docs to come
    """
    test = get_type('GiB', 'IEC')
    assert convert_size(SIZE, test['code'], 'B') == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code']) == SIZE  # nosec: B101


def test_gigabyte_si():
    """
    Docs to come
    """
    test = get_type('GB', 'SI')
    assert convert_size(SIZE, test['code'], 'B', True) == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code'], True) == SIZE  # nosec: B101


def test_terabyte():
    """
    Docs to come
    """
    test = get_type('TiB', 'IEC')
    assert convert_size(SIZE, test['code'], 'B') == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code']) == SIZE  # nosec: B101


def test_terabyte_si():
    """
    Docs to come
    """
    test = get_type('TB', 'SI')
    assert convert_size(SIZE, test['code'], 'B', True) == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code'], True) == SIZE  # nosec: B101


def test_petabyte():
    """
    Docs to come
    """
    test = get_type('PiB', 'IEC')
    assert convert_size(SIZE, test['code'], 'B') == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code']) == SIZE  # nosec: B101


def test_petabyte_si():
    """
    Docs to come
    """
    test = get_type('PB', 'SI')
    assert convert_size(SIZE, test['code'], 'B', True) == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code'], True) == SIZE  # nosec: B101


def test_exabyte():
    """
    Docs to come
    """
    test = get_type('EiB', 'IEC')
    assert convert_size(SIZE, test['code'], 'B') == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code']) == SIZE  # nosec: B101


def test_exabyte_si():
    """
    Docs to come
    """
    test = get_type('EB', 'SI')
    assert convert_size(SIZE, test['code'], 'B', True) == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code'], True) == SIZE  # nosec: B101


def test_zettabyte():
    """
    Docs to come
    """
    test = get_type('ZiB', 'IEC')
    assert convert_size(SIZE, test['code'], 'B') == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code']) == SIZE  # nosec: B101


def test_zettabyte_si():
    """
    Docs to come
    """
    test = get_type('ZB', 'SI')
    assert convert_size(SIZE, test['code'], 'B', True) == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code'], True) == SIZE  # nosec: B101


def test_yottabyte():
    """
    Docs to come
    """
    test = get_type('YiB', 'IEC')
    assert convert_size(SIZE, test['code'], 'B') == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code']) == SIZE  # nosec: B101


def test_yottabyte_si():
    """
    Docs to come
    """
    test = get_type('YB', 'SI')
    assert convert_size(SIZE, test['code'], 'B', True) == test['bytes']  # nosec: B101
    assert convert_size(test['bytes'], 'B', test['code'], True) == SIZE  # nosec: B101
