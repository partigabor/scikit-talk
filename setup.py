#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'speach>=0.1a9.post2', 'pylangacq>=0.15.0']

test_requirements = [ ]

setup(
    author="Gabor Parti",
    author_email='gabor.parti@connect.polyu.hk',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Scikit-talk helps to process real-world conversational speech data.",
    entry_points={
        'console_scripts': [
            'scikit_talk=scikit_talk.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='scikit_talk',
    name='scikit_talk',
    packages=find_packages(include=['scikit_talk', 'scikit_talk.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/partigabor/scikit_talk',
    version='0.0.223',
    zip_safe=False,
)
