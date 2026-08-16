"""
Nyotaswerve CRM - Desktop Launcher
Packaged as a standalone executable that runs the CRM as a local web server.
"""
import os
import sys
import webbrowser
import threading
import time
import socket

# Set Django settings before any Django imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Add the app directory to path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


def find_free_port():
    """Find a free TCP port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]


def run_migrations():
    """Run database migrations."""
    import django
    from django.core.management import call_command
    django.setup()
    print("📦 Running migrations...")
    call_command('migrate', '--noinput')
    print("✅ Migrations complete!")


def seed_demo_data():
    """Seed demo data if no deals exist."""
    import django
    django.setup()
    from deals.models import Deal
    if Deal.objects.count() == 0:
        print("🌱 Seeding demo data...")
        try:
            from seed_data import seed
            seed()
            print("✅ Demo data created!")
        except Exception as e:
            print(f"⚠️ Could not seed data: {e}")


def open_browser(port):
    """Open browser to the CRM."""
    time.sleep(2)
    url = f'http://localhost:{port}'
    print(f"🚀 Opening {url} in your browser...")
    webbrowser.open(url)


def main():
    print("""
╔══════════════════════════════════════════╗
║        Nyotaswerve CRM Desktop           ║
║     Bitrix24-like CRM + Tally Prime      ║
╚══════════════════════════════════════════╝
    """)
    
    port = int(os.environ.get('PORT', find_free_port()))
    host = '0.0.0.0'
    
    # Use a fixed port for predictability
    if '--port' in sys.argv:
        idx = sys.argv.index('--port') + 1
        if idx < len(sys.argv):
            port = int(sys.argv[idx])
    
    print(f"📡 Starting server on http://localhost:{port}")
    print(f"👤 Login: admin / admin123")
    print(f"📋 Press Ctrl+C to stop the server\n")
    
    # Run setup
    try:
        run_migrations()
        seed_demo_data()
    except Exception as e:
        print(f"⚠️ Setup warning: {e}")
    
    # Open browser in background
    threading.Thread(target=open_browser, args=(port,), daemon=True).start()
    
    # Start Django server
    from django.core.management import call_command
    sys.argv = ['manage.py', 'runserver', f'{host}:{port}', '--noreload']
    call_command('runserver', f'{host}:{port}', '--noreload')


if __name__ == '__main__':
    main()