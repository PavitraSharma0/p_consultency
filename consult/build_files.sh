#!/bin/bash
echo "Building Django assets for Vercel deployment..."
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "Build finished successfully."
