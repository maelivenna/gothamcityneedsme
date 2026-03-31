import os
import sys

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(base_dir)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()