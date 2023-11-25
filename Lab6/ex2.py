import os

directory_path = "C:/Users/admin/PycharmProjects/lab6/ex2"

if os.path.exists(directory_path):
    files = os.listdir(directory_path)
    files.sort()
    count = 1
    for file in files:
        file_extension = os.path.splitext(file)[1]
        new_file_name = "file" + str(count) + file_extension
        try:
            os.rename(
                os.path.join(directory_path, file),
                os.path.join(directory_path, new_file_name),
            )
            count += 1
        except Exception as e:
            print(f"Error at {file}: {e}")
else:
    print(f"Directory {directory_path} does not exist.")
