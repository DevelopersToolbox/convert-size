"""
Documentation to go here
"""

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
                    'name': 'Kilobyte',
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


def test_zero_bytes():
    """
    Test 0 bytes - Default
    """
    errors = []

    if convert_size(0, 'B', 'MiB') != 0:
        errors.append('Test 1 failed')
    if convert_size(0, 'B', 'MB', True) != 0:
        errors.append('Test 2 failed')
    if convert_size(0, 'B', 'MiB', False) != 0:
        errors.append('Test 3 failed')
    if convert_size_iec(0, 'B', 'MiB') != 0:
        errors.append('Test 4 failed')
    if convert_size_si(0, 'B', 'MB') != 0:
        errors.append('Test 5 failed')

    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_invalid_options():
    """
    Test passing invalid option
    """
    errors = []

    try:
        convert_size(SIZE, 'B', 'MB')
    except ValueError:
        pass
    else:
        errors.append('Test 1 failed')
    try:
        convert_size(SIZE, 'B', 'MiB', True)
    except ValueError:
        pass
    else:
        errors.append('Test 2 failed')
    try:
        convert_size(SIZE, 'B', 'MB', False)
    except ValueError:
        pass
    else:
        errors.append('Test 1 failed')
    try:
        convert_size_iec(SIZE, 'B', 'MB')
    except ValueError:
        pass
    else:
        errors.append('Test 1 failed')
    try:
        convert_size_si(SIZE, 'B', 'MiB')
    except ValueError:
        pass
    else:
        errors.append('Test 1 failed')

    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_get_name_from_code():
    """
    Test 0 bytes password
    """
    errors = []
    count = 0

    for t in tests:
        count += 1
        if get_name_from_code(t['IEC']['code']) != t['IEC']['name']:
            errors.append(f"Test {count} {t['IEC']['code']} failed")
        if get_name_from_code(t['SI']['code'], True) != t['SI']['name']:
            errors.append(f"Test {count} {t['SI']['code']} failed")
        if get_name_from_code(t['IEC']['code'], False) != t['IEC']['name']:
            errors.append(f"Test {count} {t['IEC']['code']} failed")
        if get_name_from_code_iec(t['IEC']['code']) != t['IEC']['name']:
            errors.append(f"Test {count} {t['IEC']['code']} failed")
        if get_name_from_code_si(t['SI']['code']) != t['SI']['name']:
            errors.append(f"Test {count} {t['SI']['code']} failed")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_convert_size_to_bytes():
    """
    Test 0 bytes password
    """
    errors = []
    count = 0
    size = 1

    for t in tests:
        count += 1

        if convert_size(size, t['IEC']['code'], 'B') != t['IEC']['bytes']:
            errors.append(f"Test {count} {t['IEC']['code']} failed")
        if convert_size(size, t['SI']['code'], 'B', True) != t['SI']['bytes']:
            errors.append(f"Test {count} {t['SI']['code']} failed")
        if convert_size(size, t['IEC']['code'], 'B', False) != t['IEC']['bytes']:
            errors.append(f"Test {count} {t['IEC']['code']} failed")
        if convert_size_iec(size, t['IEC']['code'], 'B') != t['IEC']['bytes']:
            errors.append(f"Test {count} {t['IEC']['code']} failed")
        if convert_size_si(size, t['SI']['code'], 'B') != t['SI']['bytes']:
            errors.append(f"Test {count} {t['SI']['code']} failed")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_convert_size_to_bytes_and_back():
    """
    Test 0 bytes password
    """
    errors = []
    count = 0
    size = 1

    for t in tests:
        count += 1

        bytes = convert_size(size, t['IEC']['code'], 'B')
        if convert_size(bytes, 'B', t['IEC']['code']) != size:
            errors.append(f"Test {count} {t['IEC']['code']} failed - {bytes} vs {size}")

        bytes = convert_size(size, t['SI']['code'], 'B', True)
        if convert_size(bytes, 'B', t['SI']['code'], True) != size:
            errors.append(f"Test {count} {t['SI']['code']} failed - {bytes} vs {size}")

        bytes = convert_size(size, t['IEC']['code'], 'B', False)
        if convert_size(bytes, 'B', t['IEC']['code'], False) != size:
            errors.append(f"Test {count} {t['IEC']['code']} failed - {bytes} vs {size}")

        bytes = convert_size_iec(size, t['IEC']['code'], 'B')
        if convert_size_iec(bytes, 'B', t['IEC']['code']) != size:
            errors.append(f"Test {count} {t['IEC']['code']} failed - {bytes} vs {size}")

        bytes = convert_size_si(size, t['SI']['code'], 'B')
        if convert_size_si(bytes, 'B', t['SI']['code']) != size:
            errors.append(f"Test {count} {t['SI']['code']} failed - {bytes} vs {size}")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
