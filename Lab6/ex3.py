import os
import sys

try:
    directory_path = sys.argv[1]
    total_size = 0

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size

    print(f"Total size: {total_size} BYTES")

except IndexError:
    print("Type the path in terminal.")

except FileNotFoundError:
    print("Directory not found.")

except PermissionError:
    print("You don't have access.")

except Exception as e:
    print(f"Ops, error: {e}")

# python ex3.py C:\Users\admin\PycharmProjects\lab6
