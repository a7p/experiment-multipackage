from setuptools import setup, find_packages

LONG_DESCRIPTION = """

"""

setup(
    version='0.0.1',
    name='a_package',
    author='the Author',
    author_email='authors@email.de',
    description='bla!',
    long_description=LONG_DESCRIPTION,
    url='',
    packages=find_packages(where="./", exclude=['*/src', ]),
    package_dir={"": "./"},
    zip_safe=True,
    keywords="",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.6',
    ],
)
