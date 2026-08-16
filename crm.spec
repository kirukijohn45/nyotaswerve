# -*- mode: python ; coding: utf-8 -*-
"""
Nyotaswerve CRM - PyInstaller spec for Windows executable.
Packages the Django CRM as a standalone desktop application.
"""
import os
import sys
from PyInstaller.utils.hooks import collect_all, collect_submodules, collect_data_files

# Paths
base_dir = os.path.dirname(os.path.abspath(__file__))

# Collect Django data files (templates, static, migrations)
datas = [
    (os.path.join(base_dir, 'templates'), 'templates'),
    (os.path.join(base_dir, 'static'), 'static'),
    (os.path.join(base_dir, 'config'), 'config'),
    (os.path.join(base_dir, 'accounts'), 'accounts'),
    (os.path.join(base_dir, 'contacts'), 'contacts'),
    (os.path.join(base_dir, 'leads'), 'leads'),
    (os.path.join(base_dir, 'deals'), 'deals'),
    (os.path.join(base_dir, 'tasks'), 'tasks'),
    (os.path.join(base_dir, 'products'), 'products'),
    (os.path.join(base_dir, 'invoices'), 'invoices'),
    (os.path.join(base_dir, 'tally'), 'tally'),
    (os.path.join(base_dir, 'dashboard'), 'dashboard'),
    (os.path.join(base_dir, 'seed_data.py'), '.'),
    (os.path.join(base_dir, 'requirements.txt'), '.'),
]

# Collect all Django-related hidden imports
hidden_imports = [
    'django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'import_export',
    'django.forms',
    'PIL',
    'PIL._imaging',
    'PIL.Image',
    'sqlparse',
    'asgiref',
    'whitenoise',
    'accounts',
    'contacts',
    'leads',
    'deals',
    'tasks',
    'products',
    'invoices',
    'tally',
    'dashboard',
    'config',
]

# Collect submodules for Django
for mod in ['django', 'rest_framework', 'corsheaders', 'django_filters', 'import_export']:
    try:
        hidden_imports.extend(collect_submodules(mod))
    except:
        pass

block_cipher = None

a = Analysis(
    ['crm_launcher.py'],
    pathex=[base_dir],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'scipy',
        'pandas',
        'notebook',
        'jupyter',
        'test',
        'unittest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='NyotaswerveCRM',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window (GUI app)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

# Also create a console version for debugging
exe_debug = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='NyotaswerveCRM_console',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # With console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

# Also build the console version
coll = COLLECT(
    exe_debug,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='NyotaswerveCRM',
)