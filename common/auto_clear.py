import os
import shutil
def autoClear(n):
    dir = f"{os.path.dirname(__file__)}/testReport/"
    file_list = os.listdir(dir)
    print(file_list)
    file_list.sort(key=lambda x: os.path.getmtime(dir+x))
    print(file_list[:n])
    for file in file_list[:n]:
        shutil.rmtree(dir+file)

