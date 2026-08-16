# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = ['django', 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'django.contrib.humanize', 'rest_framework', 'corsheaders', 'django_filters', 'import_export', 'PIL', 'PIL._imaging', 'sqlparse', 'asgiref', 'whitenoise', 'accounts', 'contacts', 'leads', 'deals', 'tasks', 'products', 'invoices', 'tally', 'dashboard', 'config']
hiddenimports += collect_submodules('django')


a = Analysis(
    ['crm_launcher.py'],
    pathex=[],
    binaries=[],
    datas=[('templates', 'templates'), ('static', 'static'), ('config', 'config'), ('accounts', 'accounts'), ('contacts', 'contacts'), ('leads', 'leads'), ('deals', 'deals'), ('tasks', 'tasks'), ('products', 'products'), ('invoices', 'invoices'), ('tally', 'tally'), ('dashboard', 'dashboard'), ('seed_data.py', '.'), ('requirements.txt', '.')],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='NyotaswerveCRM',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='NyotaswerveCRM',
)
