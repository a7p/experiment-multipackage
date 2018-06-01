# An experiment on python packaging and pycharm

for developing install packages with `pip install -e` - caution - this behaves differently than real package installation in some ways, e.g. excludes in setup.py are ignored (in fact it's not packaging at all).



## Switch off these in PyCharm (PythonConsole) to avoid PyCharm looking in places it should not.

add content-root to python-path
add source-roots to python-path
