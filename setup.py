from setuptools import find_packages, setup

setup(
    name='pyguard',
    packages=find_packages(),
    version='0.0.1',
    author='Joao Teixeira',
    url='https://github.com/joaoteixeira88/pyguard',
    license='Copyright',
    author_email='joaopteixeira58@gmail.com',
    description='Guard is a fluent argument validation library that is intuitive, fast and extensible.',
    install_requires=open('requirements.txt').readlines()
)