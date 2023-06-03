from setuptools import setup
setup(
name='mtraker',
version='1.0',
description='Provides a decorator for memory usage tracking. The part of FOSS course.'
    license='MIT',
    author='Nastya Kazanceva',
    author_email='nastya_kaz5@mail.ru',
    url='https://github.com/vaninjaa/123',
        packages=['mtracker'],
        install_requires=[], # it is empty since we use standard python library
        extras_require={
            'test': [
                'pytest',
                'coverage',
            ],
    },
    python_requires='>=3',
)

import tracemalloc
def execute_and_get_memory_usage(function, *args, **kwargs):
    tracemalloc.start()
    before = tracemalloc.get_traced_memory()
    result = function(*args, **kwargs)
    after = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"According to tracemalloc: { after[1] - before[1]} ")
    return result

import pytest
from mtracker.mtracker import execute_and_get_memory_usage
def _generate_list(n):
    lst = []
    for i in range(n):
        lst.append(i)
    return lst

def test_no_change():
    n = 10
    lst1 = _generate_list(n)
    lst2 = execute_and_get_memory_usage(_generate_list, n)
    assert len(lst1) == len(lst2)
    for l1, l2 in zip(lst1, lst2):
        assert l1 == l2
