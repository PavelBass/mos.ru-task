import os

from setuptools import (
    find_packages,
    setup,
)

setup(
    name='mosru_task',
    version='1.0.0',
    author='Pavel Bass',
    author_email='statgg@gmail.com',
    description='mos.ru job challenge',
    entry_points={
        'console_scripts': [
            'mosru_task=mosru_task.cli:cli',
        ],
    },
    long_description=open(os.path.join(os.path.dirname(__file__), 'README_RU.md')).read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'aiohttp==3.5.1',
        'click==7.0',
        'ujson>=1.35',
    ],
    extras_require={
        'test': [
            'pycodestyle',
            'pylint',
            'pylint-quotes',
            'pytest',
            'pytest-cov',
            'pytest-mock',
            'pytest-asyncio',
            'diff-cover',
        ],
    },
)
