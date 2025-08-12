#!/bin/bash
# Create symlink so python command works
ln -sf /usr/bin/python3.9 /usr/local/bin/python
python3.9 -m pip install -r requirements-vercel.txt && cd portfolio && python3.9 manage.py collectstatic --noinput
