import sys
from pathlib import Path

# Добавляем src в путь поиска
sys.path.append(str(Path(__file__).parent / "src"))

from pandas_code.comp.hour1 import go_start_pd


if __name__ == '__main__':
    print('start main -->')
    go_start_pd()