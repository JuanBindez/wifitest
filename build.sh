#!/bin/bash

git add .
git commit -m 'update'
git push -u origin main
git tag v0.1.9
git push --tag
make clean
make upload
