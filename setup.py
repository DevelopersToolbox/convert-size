from codecs import open
from os import path
from setuptools import setup

VERSION = '0.1.0'
DESCRIPTION = 'Convert one file size type to another'

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'pypi.md'), encoding='utf-8') as f:
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
        packages=['convertsize'],
        install_requires=[],
        keywords=['python', 'convert_size'],
        url='https://github.com/DevelopersToolbox/convert-size',

        project_urls={
            ' Source': 'https://github.com/DevelopersToolbox/convert-size',
            ' Tracker': 'https://github.com/DevelopersToolbox/convert-size/issues/',
            ' Documentation': 'https://github.com/DevelopersToolbox/convert-size',
            ' Funding': 'https://ko-fi.com/wolfsoftware',
            ' Say Thanks!': 'https://saythanks.io/to/TGWolf',
        },

        classifiers= [
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Topic :: Software Development',
        ]
)
