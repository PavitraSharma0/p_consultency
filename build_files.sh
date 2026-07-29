#!/bin/bash
echo "Building Django assets for Vercel deployment..."
python3 -m pip install -r requirements.txt
if [ -f "consult/manage.py" ]; then
    python3 consult/manage.py collectstatic --noinput --clear
elif [ -f "manage.py" ]; then
    python3 manage.py collectstatic --noinput --clear
fi
echo "Build finished successfully."
