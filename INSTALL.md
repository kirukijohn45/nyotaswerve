# Nyotaswerve CRM - Installation Guide

## 🪟 Windows Users (Get a .exe)

### Option 1: Build your own .exe (recommended)
1. Install **Python 3.10+** from [python.org](https://python.org)
2. Download this project as ZIP or clone it
3. Double-click **`build_windows.bat`**
4. Wait 3-5 minutes — you'll get `dist\NyotaswerveCRM.exe`
5. Double-click the `.exe` to run the CRM!
6. Your browser opens at `http://localhost:8000`
7. Login: **admin** / **admin123**

### Option 2: Run without building
1. Install Python 3.10+
2. Open Command Prompt in the project folder
3. Run:
```bash
pip install -r requirements.txt
python crm_launcher.py
```
4. Open http://localhost:8000

## 🐧 Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python crm_launcher.py
```

## 🐳 Docker (any OS)
```bash
docker-compose up -d
```
Then open http://localhost:8000

---

## Connecting Tally Prime
1. On your Tally machine: **F12 → Allow Remote Requests → Yes**
2. In the CRM, go to **Tally Sync → Test Connection**
3. Once connected, sync ledgers and invoices automatically

Credentials: **admin** / **admin123**