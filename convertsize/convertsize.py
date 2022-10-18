"""
Documentation to go here
"""

# IEC based values
size_codes_iec = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')
size_names_iec = ('Byte', 'Kibibyte', 'Mebibyte', 'Gibibyte', 'Tebibyte', 'Pebibyte', 'Exbibyte', 'Zebibyte', 'Yobibyte')

# SI based values
size_codes_si = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
size_names_si = ('Byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte', 'Exabyte', 'Zettabyte', 'Yottabyte')


def __in_tuple(item, stuff):
    """
    Docs to go here
    """

    return any(s.lower() == item.lower() for s in stuff)


def __get_tuple(item, stuff):
    """
    Docs to go here
    """

    new_list = [s.lower() for s in stuff]
    return new_list.index(item.lower())


def __get_index(unit, code_list):
    """
    Docs to go here
    """

    if __in_tuple(unit, code_list) is False:
        valid_types = (', '.join(code_list))
        raise ValueError(f'Invalid unit type {unit}, valid  option are: {valid_types}')
    return __get_tuple(unit, code_list)


def __calculate_new_size(size, scaler, start_index, end_index):
    """
    Docs to go here
    """

    if end_index > start_index:
        for _count in range(end_index - start_index):
            size /= scaler
    else:
        for _count in range(start_index - end_index):
            size *= scaler
    return size


def get_name_from_code_iec(unit):
    """
    Docs to go here
    """

    name_index = __get_index(unit, size_codes_iec)
    return size_names_iec[name_index]


def get_name_from_code_si(unit):
    """
    Docs to go here
    """

    name_index = __get_index(unit, size_codes_si)
    return size_names_si[name_index]


def get_name_from_code(unit, si_units = False):
    """
    Docs to go here
    """

    if si_units is True:
        return get_name_from_code_si(unit)
    return get_name_from_code_iec(unit)


def convert_size_iec(size, start_unit, end_unit):
    """
    Docs to go here
    """

    if size == 0:
        return 0

    scaler = 1024

    start_index = __get_index(start_unit, size_codes_iec)
    end_index = __get_index(end_unit, size_codes_iec)

    return __calculate_new_size(size, scaler, start_index, end_index)


def convert_size_si(size, start_unit, end_unit):
    """
    Docs to go here
    """

    if size == 0:
        return 0

    scaler = 1000

    start_index = __get_index(start_unit, size_codes_si)
    end_index = __get_index(end_unit, size_codes_si)

    return __calculate_new_size(size, scaler, start_index, end_index)


def convert_size(size, start_unit, end_unit, si_units = False):
    """
    Docs to go here
    """
    if size == 0:
        return 0

    if si_units is True:
        return convert_size_si(size, start_unit, end_unit)
    return convert_size_iec(size, start_unit, end_unit)
