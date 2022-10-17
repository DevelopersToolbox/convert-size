from setuptools import setup
from codecs import open
from os import path

VERSION = '0.0.5'
DESCRIPTION = 'Convert one file size type to another'

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='convertsize',
        version=VERSION,
        author='Wolf Software',
        author_email='<pypi@wolfsoftware.com>',
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown',
        license='MIT',
        url='https://github.com/DevelopersToolbox/convert-size',
        packages=['convertsize'],
        install_requires=[],
        keywords=['python', 'convert_size'],

        classifiers= [
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Topic :: Software Development',
        ]
)
