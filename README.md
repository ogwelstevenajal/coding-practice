# FarmStack

A responsive, scalable Django-based farm management system for small-scale farmers.

## Features
- Role-based auth (admin, farmer, agent)
- Inventory, Sales, Finance, Agricultural Practices
- Dashboard with charts (sales, yields, finances)
- REST API (DRF + schema/docs)
- PDF/Excel exports
- SMS notifications (pluggable)
- PWA (manifest + service worker)
- i18n-ready

## Quickstart

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # or edit .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Environment
See `.env` for configurable settings. To use MySQL, set `MYSQL_*` vars.

## API Docs
- Schema: `/api/schema/`
- Swagger: `/api/docs/`

## Build/Run
- Static: `python manage.py collectstatic`
- Celery: `celery -A farmstack worker -l info`
- Channels requires Redis: set `REDIS_URL`

## PWA
- Manifest at `/static/manifest.webmanifest`
- Service worker at `/static/service-worker.js`

## License
MIT