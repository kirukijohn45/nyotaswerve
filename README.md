# Nyotaswerve CRM

A **Bitrix24-like CRM system** with **Tally Prime integration** built with Django.

## ✨ Features

### CRM Core
- **Dashboard** — Sales overview, metrics, pipeline status, recent deals & invoices
- **Deals Pipeline (Kanban Board)** — Drag & drop deal management like Bitrix24
- **Leads Management** — Track leads through stages with source tracking
- **Contacts & Companies** — Manage your relationships
- **Tasks & Activities** — Follow-ups, calls, meetings, emails
- **Products & Services** — Product catalog with pricing
- **Invoices** — Billing with status tracking

### Tally Prime Integration
- **XML API Client** — Communicate with Tally Prime on port 9000
- **Ledger Sync** — Import/export ledgers between CRM and Tally
- **Sales Voucher Sync** — Push invoices as sales vouchers to Tally
- **Sync Logs** — Track all sync operations

### REST API
Full RESTful API for all modules (Deals, Contacts, Leads, Tasks, Products, Invoices)

## 🚀 Quick Start

```bash
# Create virtual environment & install
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Seed demo data
python seed_data.py

# Start server
python manage.py runserver 0.0.0.0:8000
```

Access at **http://localhost:8000**

## 🔑 Demo Credentials
- **Username:** admin  
- **Password:** admin123

## 🏗️ Architecture

```
nyotaswerve/
├── accounts/       # User authentication & profiles
├── contacts/       # Contacts & Companies
├── leads/          # Lead management
├── deals/          # Deal pipeline & Kanban board
├── tasks/          # Tasks & activities
├── products/       # Product catalog
├── invoices/       # Invoicing & billing
├── tally/          # Tally Prime XML API integration
├── dashboard/      # Main dashboard & reports
├── config/         # Django project settings
├── templates/      # HTML templates
├── static/         # Static files
└── seed_data.py    # Demo data seeder
```

## 🔗 Tally Prime Setup

1. Ensure Tally Prime is running with **Tally.NET enabled** on port 9000
2. Go to **Tally Sync** section in Nyotaswerve
3. Click **Test Connection** to verify connectivity
4. Use **Sync Ledgers** to import masters from Tally

## 🧑‍💻 API Endpoints

| Module | Endpoints |
|--------|-----------|
| Deals | `/deals/api/deals/`, `/deals/api/pipelines/`, `/deals/api/pipeline-stages/` |
| Contacts | `/contacts/api/contacts/`, `/contacts/api/companies/` |
| Leads | `/leads/api/leads/`, `/leads/api/lead-sources/` |
| Tasks | `/tasks/api/tasks/` |
| Products | `/products/api/products/`, `/products/api/categories/` |
| Invoices | `/invoices/api/invoices/`, `/invoices/api/invoice-lines/` |

## 📊 Kanban Board
The kanban board at `/deals/kanban/` provides a Bitrix24-style drag-and-drop interface for managing your deal pipeline.

## 🛠️ Tech Stack
- **Backend:** Django 5.2 + Django REST Framework
- **Frontend:** Tailwind CSS, SortableJS (drag & drop)
- **Database:** SQLite (development) / PostgreSQL (production)
- **Tally API:** XML over HTTP on port 9000