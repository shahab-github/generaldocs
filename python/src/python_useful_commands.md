#### Python Useful Commnads

To build a python package
```
python3 setup.py sdist bdist_wheel
```
To install and test the package locally
```
pip3 install dist/<nameoftheWheelFile>
```

To publish the package to PYPI
```
pip3 install setuptools wheel twine
twine upload dist/*
```
