#!/bin/bash

python3 -m py_compile $PYFILE
mv __pycache__/*.pyc ./$PYFILE'c'
chmod +x $PYFILE'c'
rmdir i_pycache__
