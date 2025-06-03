import os
import shutil
def autoClear(n):
    path = f"{os.path.dirname(os.path.dirname(__file__))}/testReport/"
    # print(f"位置：{dir}")
    file_list = os.listdir(path)
    # print(file_list)
    file_list.sort(key=lambda x: os.path.getmtime(dir+x))
    # print(file_list[n:],"\n")
    # print(len(file_list))
    if len(file_list)/2 > n:
        print(file_list[:n])
        for file in file_list[:n]:
            shutil.rmtree(dir + file)


