#!/bin/bash -e
cd ..
rm -rf dist
python setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ ./dist/*
