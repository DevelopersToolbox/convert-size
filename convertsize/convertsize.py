"""
Documentation to go here
"""


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


def __get_index(size, unit, code_list):
    """
    """

    if __in_tuple(unit, code_list) is False:
        valid_types = (', '.join(code_list))
        raise ValueError(f'Invalid unit type {unit}, valid  option are: {valid_types}')
    return __get_tuple(unit, code_list)


def __get_indexs(size, start_unit, end_unit, size_codes):
    """
    """

    start_index = __get_index(size, start_unit, size_codes)
    end_index = __get_index(size, end_unit, size_codes)

    return start_index, end_index

def __calculate_new_size(size, scaler, start_index, end_index):
    """
    """

    if end_index > start_index:
        for _count in range(end_index - start_index):
            size /= scaler
    else:
        for _count in range(start_index - end_index):
            size *= scaler
    return size


def convert_size_iec(size, start_unit, end_unit):
    """
    Docs to go here
    """

    if size == 0:
        return 0

    scaler = 1024
    size_codes = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')

    start_index, end_index = __get_indexs(size, start_unit, end_unit, size_codes)

    return __calculate_new_size(size, scaler, start_index, end_index)


def convert_size_si(size, start_unit, end_unit):
    """
    Docs to go here
    """

    if size == 0:
        return 0

    scaler = 1000
    size_codes = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')

    start_index, end_index = __get_indexs(size, start_unit, end_unit, size_codes)

    return __calculate_new_size(size, scaler, start_index, end_index)


def convert_size(size, start_unit, end_unit, si_units = False):
    """
    Docs to go here
    """
    if size == 0:
        return 0

    if si_units is True:
        return convert_size_si(size, start_unit, end_unit)
    else:
        return convert_size_iec(size, start_unit, end_unit)
