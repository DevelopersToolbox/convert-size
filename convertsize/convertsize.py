import math

def xxx(item, stuff):
    return any(s.lower() == item.lower() for s in stuff)

def yyy(item, stuff):
    new_list = [s.lower() for s in stuff]
    return new_list.index(item.lower())

def convert_size(size, start_unit, end_unit, SI = False):
    if size == 0:
        return "0"

    if SI is True:
        divisor = 1000
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    else:
        divisor = 1024
        size_name = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")

    if xxx(start_unit, size_name) is False or xxx(end_unit, size_name) is False:
        valid_types = (', '.join(size_name))
        print(f"Invalid unit type, valid  option are: {valid_types}")
        return size

    startIndex = yyy(start_unit, size_name)
    endIndex = yyy(end_unit, size_name)

    if startIndex == endIndex:
        pass
    elif endIndex > startIndex:
        for count in range(endIndex - startIndex):
            size /= divisor
    else:
        for count in range(startIndex - endIndex):
            size *= divisor

    return size
