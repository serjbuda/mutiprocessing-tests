import os
import shutil
from threading import Thread

def move_file(src, dst):
    shutil.move(src, dst)

def sort_files(path, dest_path):
    extensions = {}

    for root, dirs, files in os.walk(path):
        for file in files:
            extension = os.path.splitext(file)[1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(os.path.join(root, file))

    for extension in extensions:
        ext_path = os.path.join(dest_path, extension[1:])
        if not os.path.exists(ext_path):
            os.makedirs(ext_path)
            
        threads = []
        for file in extensions[extension]:
            dst = os.path.join(ext_path, os.path.basename(file))
            thread = Thread(target=move_file, args=(file, dst))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

if __name__ == '__main__':
    path = 'Хлам'  
    dest_path = 'Відсортовані файли'  
    sort_files(path, dest_path)
