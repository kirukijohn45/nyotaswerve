"""
Nyotaswerve CRM - Portable Application Entry Point
This is the main entry point when run as a zipapp or module.
"""
import os
import sys
import subprocess

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    os.chdir(THIS_DIR)
    sys.path.insert(0, THIS_DIR)
    
    # Launch the CRM
    import crm_launcher
    crm_launcher.main()


if __name__ == '__main__':
    main()