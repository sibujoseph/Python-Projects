python -m venv ./venv
source venv/bin/activate
pip install FastAPI
pip install unicorn
pip freeze >> requirements.txt
