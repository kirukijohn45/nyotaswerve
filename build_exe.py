#!/usr/bin/env python3
"""
Build script for Nyotaswerve CRM standalone executable.
Works on Linux and Windows (with PyInstaller).

Usage:
    python build_exe.py              # Build for current OS
    python build_exe.py --onefile    # Build single-file executable
"""

import os
import sys
import shutil
import subprocess
import platform


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)
    
    print("╔══════════════════════════════════════════╗")
    print("║   Building Nyotaswerve CRM Executable    ║")
    print("╚══════════════════════════════════════════╝")
    print(f"  OS: {platform.system()} {platform.release()}")
    print(f"  Python: {sys.version.split()[0]}")
    print()
    
    # Ensure PyInstaller is installed
    try:
        import PyInstaller
        print("✅ PyInstaller found")
    except ImportError:
        print("📦 Installing PyInstaller...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])
        print("✅ PyInstaller installed")
    
    # Determine build mode
    onefile = '--onefile' in sys.argv or '-F' in sys.argv
    console = '--console' in sys.argv or '--debug' in sys.argv
    
    # Clean previous builds
    for d in ['build', 'dist']:
        if os.path.exists(d):
            shutil.rmtree(d)
    
    # Build command - flags go AFTER the script
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        'crm_launcher.py',
        '--name', 'NyotaswerveCRM',
        '--add-data', f'templates{os.pathsep}templates',
        '--add-data', f'static{os.pathsep}static',
        '--add-data', f'config{os.pathsep}config',
        '--add-data', f'accounts{os.pathsep}accounts',
        '--add-data', f'contacts{os.pathsep}contacts',
        '--add-data', f'leads{os.pathsep}leads',
        '--add-data', f'deals{os.pathsep}deals',
        '--add-data', f'tasks{os.pathsep}tasks',
        '--add-data', f'products{os.pathsep}products',
        '--add-data', f'invoices{os.pathsep}invoices',
        '--add-data', f'tally{os.pathsep}tally',
        '--add-data', f'dashboard{os.pathsep}dashboard',
        '--add-data', f'seed_data.py{os.pathsep}.',
        '--add-data', f'requirements.txt{os.pathsep}.',
        '--hidden-import', 'django',
        '--hidden-import', 'django.contrib.admin',
        '--hidden-import', 'django.contrib.auth',
        '--hidden-import', 'django.contrib.contenttypes',
        '--hidden-import', 'django.contrib.sessions',
        '--hidden-import', 'django.contrib.messages',
        '--hidden-import', 'django.contrib.staticfiles',
        '--hidden-import', 'django.contrib.humanize',
        '--hidden-import', 'rest_framework',
        '--hidden-import', 'corsheaders',
        '--hidden-import', 'django_filters',
        '--hidden-import', 'import_export',
        '--hidden-import', 'PIL',
        '--hidden-import', 'PIL._imaging',
        '--hidden-import', 'sqlparse',
        '--hidden-import', 'asgiref',
        '--hidden-import', 'whitenoise',
        '--hidden-import', 'accounts',
        '--hidden-import', 'contacts',
        '--hidden-import', 'leads',
        '--hidden-import', 'deals',
        '--hidden-import', 'tasks',
        '--hidden-import', 'products',
        '--hidden-import', 'invoices',
        '--hidden-import', 'tally',
        '--hidden-import', 'dashboard',
        '--hidden-import', 'config',
        '--collect-submodules', 'django',
    ]
    
    if onefile:
        cmd.append('--onefile')
        print("📦 Mode: Single-file executable")
    else:
        cmd.append('--onedir')
        print("📂 Mode: Directory with dependencies")
    
    if not console:
        if platform.system() == 'Windows':
            cmd.append('--windowed')
        print("🪟 Windowed mode (no console)")
    else:
        cmd.append('--console')
        print("💻 Console mode (debug)")
    
    print(f"\n🏗️  Building... (this may take 2-5 minutes)")
    print(f"   Running PyInstaller...")
    print()
    sys.stdout.flush()
    
    try:
        subprocess.check_call(cmd)
        
        # Find the output
        dist_dir = os.path.join(base_dir, 'dist')
        exe_name = 'NyotaswerveCRM'
        
        if onefile:
            ext = '.exe' if platform.system() == 'Windows' else ''
            exe_path = os.path.join(dist_dir, f'{exe_name}{ext}')
            if os.path.exists(exe_path):
                size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"\n✅ Build successful!")
                print(f"   📍 {exe_path}")
                print(f"   📦 Size: {size_mb:.1f} MB")
        else:
            dir_path = os.path.join(dist_dir, exe_name)
            if os.path.exists(dir_path):
                # Find main executable
                ext = '.exe' if platform.system() == 'Windows' else ''
                exe_path = os.path.join(dir_path, f'{exe_name}{ext}')
                if os.path.exists(exe_path):
                    size_mb = os.path.getsize(exe_path) / (1024 * 1024)
                    print(f"\n✅ Build successful!")
                    print(f"   📍 {exe_path}")
                    print(f"   📦 Executable: {size_mb:.1f} MB")
                    
                    total = sum(os.path.getsize(os.path.join(dp, f)) for dp, dn, fn in os.walk(dir_path) for f in fn) / (1024 * 1024)
                    print(f"   📦 Total folder: {total:.1f} MB")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed with exit code {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Build error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()