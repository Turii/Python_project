import os

import yaml


def load_config():
    # Отримуємо абсолютний шлях до директорії, де знаходиться цей файл (config.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Створюємо шлях до файлу config.yaml
    config_path = os.path.join(current_dir, 'config.yaml')
    # Відкриваємо файл за абсолютним шляхом
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
#def load_config():
#    with open('config/config.yaml', 'r') as f:
#       return yaml.safe_load(f)
