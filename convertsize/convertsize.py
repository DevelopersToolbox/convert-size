"""
Documentation to go here
"""


def in_tuple(item, stuff):
    """
    Docs to go here
    """

    return any(s.lower() == item.lower() for s in stuff)


def get_tuple(item, stuff):
    """
    Docs to go here
    """

    new_list = [s.lower() for s in stuff]
    return new_list.index(item.lower())


def convert_size(size, start_unit, end_unit, si_units = False):
    """
    Docs to go here
    """
    if size == 0:
        return 0

    if si_units is True:
        divisor = 1000
        size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    else:
        divisor = 1024
        size_name = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')

    if in_tuple(start_unit, size_name) is False or in_tuple(end_unit, size_name) is False:
        valid_types = (', '.join(size_name))
        print(f'Invalid unit type, valid  option are: {valid_types}')
        return size

    start_index = get_tuple(start_unit, size_name)
    end_index = get_tuple(end_unit, size_name)

    if end_index > start_index:
        for _count in range(end_index - start_index):
            size /= divisor
    else:
        for _count in range(start_index - end_index):
            size *= divisor

    return size
