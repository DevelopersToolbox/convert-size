"""
Documentation to go here
"""

from convertsize.convertsize import convert_size

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

size = 1


def get_type(code, section = 'IEC'):
    return next((item[section] for item in tests if item[section]["code"] == code), False)


def test_byte():
    test = get_type('B', 'IEC')
    assert convert_size(size, test['code'], 'B') == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code']) == size


def test_byte_si():
    test = get_type('B', 'SI')
    assert convert_size(size, test['code'], 'B', True) == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code'], True) == size


def test_kilobyte():
    test = get_type('KiB', 'IEC')
    assert convert_size(size, test['code'], 'B') == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code']) == size


def test_kilobyte_si():
    test = get_type('KB', 'SI')
    assert convert_size(size, test['code'], 'B', True) == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code'], True) == size


def test_megabyte():
    test = get_type('MiB', 'IEC')
    assert convert_size(size, test['code'], 'B') == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code']) == size


def test_megabyte_si():
    test = get_type('MB', 'SI')
    assert convert_size(size, test['code'], 'B', True) == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code'], True) == size


def test_gigabyte():
    test = get_type('GiB', 'IEC')
    assert convert_size(size, test['code'], 'B') == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code']) == size


def test_gigabyte_si():
    test = get_type('GB', 'SI')
    assert convert_size(size, test['code'], 'B', True) == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code'], True) == size


def test_terabyte():
    test = get_type('TiB', 'IEC')
    assert convert_size(size, test['code'], 'B') == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code']) == size


def test_terabyte_si():
    test = get_type('TB', 'SI')
    assert convert_size(size, test['code'], 'B', True) == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code'], True) == size


def test_petabyte():
    test = get_type('PiB', 'IEC')
    assert convert_size(size, test['code'], 'B') == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code']) == size


def test_petabyte_si():
    test = get_type('PB', 'SI')
    assert convert_size(size, test['code'], 'B', True) == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code'], True) == size


def test_exabyte():
    test = get_type('EiB', 'IEC')
    assert convert_size(size, test['code'], 'B') == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code']) == size


def test_exabyte_si():
    test = get_type('EB', 'SI')
    assert convert_size(size, test['code'], 'B', True) == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code'], True) == size


def test_zettabyte():
    test = get_type('ZiB', 'IEC')
    assert convert_size(size, test['code'], 'B') == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code']) == size


def test_zettabyte_si():
    test = get_type('ZB', 'SI')
    assert convert_size(size, test['code'], 'B', True) == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code'], True) == size


def test_yottabyte():
    test = get_type('YiB', 'IEC')
    assert convert_size(size, test['code'], 'B') == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code']) == size


def test_yottabyte_si():
    test = get_type('YB', 'SI')
    assert convert_size(size, test['code'], 'B', True) == test['bytes']
    assert convert_size(test['bytes'], 'B', test['code'], True) == size
