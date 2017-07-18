from distutils.core import setup
setup(
    name='scrapy-twitter',
    version='1',
    description='Twitter API wrapper for scrapy',
    url='https://github.com/joseangeldiazg/scrapy-twitter',
    author='Jose Angel Diaz Garcia',
    author_email='joseangeldiazg',
    license='MIT',
    py_modules=['twitterutils'],
    install_requires=[
        'python-twitter'
    ],
    zip_safe=False)
