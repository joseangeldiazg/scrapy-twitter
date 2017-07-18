"""
Setup script for PyPi
"""

from distutils.core import setup
setup(
    name='scrapy-twitter',
    version='1',
    description='Crawler for twitter',
    url='https://github.com/joseangeldiazg/scrapy-twitter',
    author='Jose Angel Diaz',
    author_email='joseadiazg02@correo.ugr.es',
    license='MIT',
    py_modules=['scrapy_twitter'],
    install_requires=[
        'python-twitter'
    ],
    zip_safe=False)
