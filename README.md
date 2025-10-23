Clone dự án
```bash
git clone https://github.com/TwxnhNGUXN/project_web_ecommerce.git
cd project_web_ecommerce
python -m venv env
env\Scripts\activate      # (Windows)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
