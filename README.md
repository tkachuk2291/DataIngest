# DataIngest
Web application for uploading XLS/XLSX files and viewing aggregated impressions by year.

## Requirements

- Python 3.12+

## Setup

**1. Clone and enter the project**

```bash
git clone https://github.com/tkachuk2291/DataIngest

cd DataIngest
```

**2. Create virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install Django djangorestframework djangorestframework-simplejwt pandas openpyxl xlrd python-dotenv
```

**4. Configure environment**

```bash
cp .env.example .env
```

Edit `.env`:

```
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Generate a secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**5. Apply migrations**

```bash
python manage.py migrate
```

**6. Create first admin user**

```bash
python manage.py createsuperuser
```

**7. Run**

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/admin/`, login for user that was created

After that new users can be created in two ways:

**Option 1 — Admin panel**

`http://127.0.0.1:8000/admin/user/customuser/add/` — fill in username, email, password and role.

**Option 2 — API (curl)**

Get admin token:
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "your_password"}'
```

Create user:
```bash
curl -X POST http://127.0.0.1:8000/users/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <access_token>" \
  -d '{"username": "newuser", "email": "newuser@example.com", "password": "password123", "role": "user"}'
```

Open `http://127.0.0.1:8000/`

## Roles

- User — can upload files and view statistics
- Admin — all of the above plus access to the admin panel

Role is set in the admin panel under Users.

## Admin panel

Available at `/admin/` for Admin users.

- Load files — email, filename, date, upload status, error message
- Users — email, registration date, role
- Raw data — full uploaded data, filterable by user

## File format

The uploaded file must contain these columns (any order, case-insensitive):

Advertiser, Brand, Start, End, Format, Platform, Impr
