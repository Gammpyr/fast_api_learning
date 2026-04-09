import json
from json import JSONDecodeError
from pathlib import Path

DATA_DIR = Path("app/data")
DATA_DIR.mkdir(exist_ok=True)


def get_data_from_file(filename="test_data"):
    """Получаем данные из файла"""
    filepath = DATA_DIR / f"{filename}.json"

    if not filepath.exists():
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except JSONDecodeError:
            return []

    return data


def save_data_to_file(data: dict, filename: str = "test_data"):
    """Сохраняет данные в файл, дополняя его если возможно"""
    filepath = DATA_DIR / f"{filename}.json"

    saved_data = get_data_from_file(filename)

    updated_data = saved_data + [data]

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(updated_data, f, ensure_ascii=False, indent=4)

    print(f"Данные сохранены в файл {filepath}")
