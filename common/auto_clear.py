import os
import shutil


def autoClear(n):
    report_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "testReport")
    print(f"报告目录位置：{report_dir}")

    if not os.path.exists(report_dir):
        print("报告目录不存在，无需清理。")
        return

    file_list = os.listdir(report_dir)
    file_list = [f for f in file_list if os.path.isdir(os.path.join(report_dir, f))]

    # 按文件夹最后修改时间排序
    file_list.sort(key=lambda x: os.path.getmtime(os.path.join(report_dir, x)))

    # 如果超过 n 个，就删除最早的
    if len(file_list) > n:
        delete_list = file_list[:len(file_list) - n]
        print(f"清理以下报告目录：{delete_list}")
        for folder in delete_list:
            folder_path = os.path.join(report_dir, folder)
            shutil.rmtree(folder_path)
            print(f"已删除：{folder_path}")
    else:
        print("报告数量未超出限制，无需清理。")

