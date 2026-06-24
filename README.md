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
pip install -r requirements.txt
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

**6. Create admin user**

```bash
python manage.py createsuperuser
```

Then open `/admin/`, find the user and set Role to Admin.

**7. Run**

```bash
python manage.py runserver
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
