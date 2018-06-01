from setuptools import setup, find_packages

LONG_DESCRIPTION = """

"""

setup(
    version='0.0.1',
    name='master_data',
    author='Albrecht Muehlenschulte',
    author_email='albrecht@a7p.org',
    description='bla!!!',
    long_description=LONG_DESCRIPTION,
    url='',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    zip_safe=True,
    keywords="",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.6',
        '"License :: OSI Approved :: GPL",'
    ],
)
