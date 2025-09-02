import os
import shutil
import argparse
from pathlib import Path

def copy_and_sort_files(source_dir: Path, dest_dir: Path):
    """
    Рекурсивно обходить всі файли та директорії у source_dir,
    копіює файли у dest_dir у відповідні підтеки за розширенням.
    """
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                # Рекурсивний виклик для обробки підкаталогів
                copy_and_sort_files(item, dest_dir)
            elif item.is_file():
                # Визначення розширення файлу (без крапки), або "no_extension"
                ext = item.suffix[1:].lower() or "no_extension"
                target_subdir = dest_dir / ext

                # Створення підкаталогу, якщо він не існує
                target_subdir.mkdir(parents=True, exist_ok=True)

                try:
                    # Копіювання файлу в відповідну піддиректорію
                    shutil.copy2(item, target_subdir / item.name)
                except PermissionError:
                    print(f"❌ Permission denied: {item}")
                except Exception as e:
                    print(f"❌ Error copying {item}: {e}")
    except FileNotFoundError:
        print(f"❌ Directory not found: {source_dir}")
    except Exception as e:
        print(f"❌ Error accessing {source_dir}: {e}")

def main():
    # Ініціалізація парсера аргументів командного рядка
    parser = argparse.ArgumentParser(
        description="Recursively sort and copy files by extension."
    )
    parser.add_argument(
        "source", type=str, help="Source directory"
    )
    parser.add_argument(
        "destination", type=str, nargs="?", default="dist",
        help="Destination directory (default: dist)"
    )
    args = parser.parse_args()

    # Отримання абсолютних шляхів
    source_path = Path(args.source).resolve()
    destination_path = Path(args.destination).resolve()

    # Перевірка, що вихідна директорія існує
    if not source_path.exists() or not source_path.is_dir():
        print(f"❌ Source directory does not exist or is not a directory: {source_path}")
        return

    # Створення директорії призначення (якщо не існує)
    destination_path.mkdir(parents=True, exist_ok=True)

    print(f"🔄 Processing files from {source_path} to {destination_path}...")
    
    # Запуск основної логіки сортування
    copy_and_sort_files(source_path, destination_path)

    print("✅ All files have been sorted and copied successfully.")

# Точка входу в програму
if __name__ == "__main__":
    main()
