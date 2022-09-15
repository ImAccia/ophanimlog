from setuptools import setup, find_packages


setup(
    name='ophanimlog',
    packages=['ophanimlog'],
    version='1.2.4',
    license='GPL V3.0',
    author="Alex Acciarri",
    author_email='accia.ale@gmail.com',
    package_dir={'': 'src'},
    url='https://github.com/ImAccia/ophanimlog',
    keywords='Log Logging Logger Py Python Easy Simple',
    install_requires=[
          'colorama',
      ],

)