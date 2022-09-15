from setuptools import setup, find_packages


setup(
    name='ophanimlog',
    packages=['ophanimlog'],
    version='1.2.3',
    license='GNU V3',
    author="Alex Acciarri",
    author_email='accia.ale@gmail.com',
    package_dir={'': 'src'},
    url='https://github.com/ImAccia/easylog',
    keywords='Log Logging Logger Py Python Easy Simple',
    install_requires=[
          'colorama',
      ],

)