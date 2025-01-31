#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md', encoding='utf-8') as history_file:
    history = history_file.read()

install_requires = [
    'appdirs>=1.3,<2',
    'boto3>=1.15.0,<2',
    'botocore>=1.18,<2',
    'compress-pickle>=1.2.0,<3',
    'humanfriendly>=8.2,<11',
    "numpy>=1.18.0,<1.20.0;python_version<'3.7'",
    "numpy>=1.20.0,<2;python_version>='3.7'",
    'pandas>=1.1.3,<2',
    "pomegranate>=0.13.4,<0.14.2;python_version<'3.7'",
    "pomegranate>=0.14.1,<0.14.7;python_version>='3.7'",
    'psutil>=5.7,<6',
    'scikit-learn>=0.24,<2',
    'scipy>=1.5.4,<2',
    'tabulate>=0.8.3,<0.9',
    'torch>=1.8.0,<2',
    'tqdm>=4.15,<5',
    'XlsxWriter>=1.2.8,<4',
    'rdt>=0.6.1,<0.7',
    'sdmetrics>=0.4.1,<0.5',
    'sdv>=0.13.0',
]


dask_requires = [
    'dask',
    'distributed',
]


ydata_requires = [
    # preferably install using make install-ydata
    'ydata-synthetic==0.6.1',
]

gretel_requires = [
    'gretel-synthetics==0.17',
    'wheel~=0.35',
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

tests_require = [
    'pytest>=3.4.2',
    'pytest-cov>=2.6.0',
    'jupyter>=1.0.0,<2',
    'rundoc>=0.4.3,<0.5',
]

development_requires = [
    # general
    'bumpversion>=0.5.3,<0.6',
    'pip>=9.0.1',
    'watchdog>=0.8.3,<0.11',

    # style check
    'flake8>=3.7.7,<4',
    'isort>=4.3.4,<5',

    # fix style issues
    'autoflake>=1.1,<2',
    'autopep8>=1.4.3,<2',

    # distribute on PyPI
    'twine>=1.10.0,<4',
    'wheel>=0.30.0',

    # Advanced testing
    'coverage>=4.5.1,<6',
    'tox>=2.9.1,<4',
    'importlib-metadata>=3.6',

    # Invoke
    'invoke',
]

setup(
    author='MIT Data To AI Lab',
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    description=(
        'A framework to benchmark the performance of synthetic data generators '
        'for non-temporal tabular data'
    ),
    entry_points={
        'console_scripts': [
            'sdgym=sdgym.__main__:main'
        ],
    },
    extras_require={
        'all': development_requires + tests_require + dask_requires + gretel_requires,
        'dev': development_requires + tests_require + dask_requires,
        'test': tests_require,
        'gretel': gretel_requires,
        'dask': dask_requires,
    },
    include_package_data=True,
    install_requires=install_requires,
    license='MIT license',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    keywords='machine learning synthetic data generation benchmark generative models',
    name='sdgym',
    packages=find_packages(include=['sdgym', 'sdgym.*']),
    python_requires='>=3.6,<3.10',
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/sdv-dev/SDGym',
    version='0.5.1.dev0',
    zip_safe=False,
)
