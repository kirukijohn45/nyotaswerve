#!/usr/bin/env python3
"""
Nyotaswerve CRM - Portable Launcher
This is the entry point for the standalone executable and zipapp.
"""
import os
import sys
import socket
import threading
import time
import webbrowser

# Set the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ.setdefault('DJANGO_ALLOW_ASYNC_UNSAFE', 'true')


def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]


def print_banner(port):
    print(r"""
   ╔══════════════════════════════════════════╗
   ║        Nyotaswerve CRM Desktop           ║
   ║     Bitrix24-like CRM + Tally Prime      ║
   ╚══════════════════════════════════════════╝
    """)
    print(f"  🌐  Server: http://localhost:{port}")
    print(f"  👤  Login:  admin / admin123")
    print(f"  ⏹️   Press Ctrl+C to stop")
    print()


def run_server(port):
    """Start the Django dev server."""
    from django.core.management import call_command
    sys.argv = ['manage.py', 'runserver', f'0.0.0.0:{port}', '--noreload']
    call_command('runserver', f'0.0.0.0:{port}', '--noreload')


def setup():
    """Run migrations and seed data."""
    import django
    from django.core.management import call_command
    
    django.setup()
    
    print("  📦 Running migrations...")
    call_command('migrate', '--noinput')
    
    from deals.models import Deal
    if Deal.objects.count() == 0:
        print("  🌱 Seeding demo data...")
        try:
            from seed_data import seed
            seed()
        except Exception as e:
            print(f"  ⚠️  Seed warning: {e}")
    
    print("  ✅ Ready!\n")


def open_browser_delayed(port):
    time.sleep(2)
    webbrowser.open(f'http://localhost:{port}')


def main():
    import django
    
    port = int(os.environ.get('PORT', 8000))
    
    # Try to find a free port
    try:
        port = find_free_port()
    except:
        pass
    
    print_banner(port)
    setup()
    
    # Open browser
    threading.Thread(target=open_browser_delayed, args=(port,), daemon=True).start()
    
    # Start server
    run_server(port)


if __name__ == '__main__':
    main()