[![build status](https://img.shields.io/github/workflow/status/DevelopersToolbox/convert-size/CICD%20Pipeline/master?style=for-the-badge)](https://github.com/DevelopersToolbox/convert-size/actions/workflows/cicd-pipeline.yml)
[![codecov](https://img.shields.io/codecov/c/gh/DevelopersToolbox/convert-size?style=for-the-badge)](https://codecov.io/gh/DevelopersToolbox/convert-size)

## Overview

This is a simple Python package to convert a size (e.g. filesize) from one scale to another. You can scale in either direction.

### Usage

The main usage is the same no matter how you access the converter.

```shell
new_size = converter_function(original_size, original_code, target_code)
```

| Parameter      | Type    | Required?     | Example Value | Purpose         |
| -------------- | ------- | ------------- | :-----------: | --------------- |
| original\_size | Integer | Yes           | 123456789     |               | The current size without any unit type. |
| original\_code | String  | Yes           | 'MiB'         |               | The code for the original type. |
| target\_code   | String  | Yes           | 'GiB'         |               | The code for the target type.   |

> The 2 codes (original &amp; target) are dependant on if you are using IEC or SI mode, so make sure you use the correct one. A ValueError exception is throw if the code is not located.

#### IEC Based

For IEC based conversations the following values are defined.

```shell
scaler = 1024
size_codes = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')
size_name = ('Byte', 'Kibibyte', 'Mebibyte', 'Gibibyte', 'Tebibyte', 'Pebibyte', 'Exbibyte', 'Zebibyte', 'Yobibyte')
```

To make use of the converter, simply use the following code:

```shell
from convertsize.convertsize import convert_size_iec

print(convert_size_iec(123456789, 'MiB', 'B'))
```

#### SI Based

For SI based conversations the following values are defined.

```shell
scaler = 1000
size_codes = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
size_name = ('Byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte', 'Exabyte', 'Zettabyte', 'Yottabyte')
```

To make use of the converter, simply use the following code:

```shell
from convertsize.convertsize import convert_size_si

print(convert_size_iec(123456789, 'MB', 'B'))
```

#### Wrapper

There is a higher level wrapper function. This function will default to IEC mode.

To make use of the converter, simply use the following code:

```shell
from convertsize.convertsize import convert_size

print(convert_size(123456789, 'MiB', 'B'))

or

print(convert_size(123456789, 'MiB', 'B', False))
```

To access SI mode then simply pass `True` to the converter.

```shell
from convertsize.convertsize import convert_size

print(convert_size(123456789, 'MB', 'B', True))
```
