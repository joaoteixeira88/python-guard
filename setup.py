from setuptools import find_packages, setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='python-parameter-guard',
    packages=find_packages(),
    python_requires='>3.0',
    version='0.1.0',
    author='Joao Teixeira',
    author_email='ervilhaman@hotmail.com',
    url='https://github.com/joaoteixeira88/python-guard',
    download_url='https://github.com/joaoteixeira88/python-guard/archive/0.1.0.tar.gz',
    keywords=['python', 'guard', 'parameters', 'exceptions'],
    license='MIT',
    description='Guard is a fluent argument validation library that is intuitive, fast and extensible.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
