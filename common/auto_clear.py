import os
import shutil

def autoClear(n, re_dir):
    report_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), re_dir)
    print(f"报告目录位置：{report_dir}")

    if not os.path.exists(report_dir):
        print("报告目录不存在，无需清理。")
        return

    # 获取所有非隐藏的文件夹
    file_list = [
        f for f in os.listdir(report_dir)
        if os.path.isdir(os.path.join(report_dir, f)) and not f.startswith(".")
    ]

    # 按修改时间升序（旧的在前）
    file_list.sort(key=lambda x: os.path.getmtime(os.path.join(report_dir, x)))

    if len(file_list) > n:
        delete_list = file_list[:len(file_list) - n]
        print(f"清理以下报告目录：{delete_list}")
        for folder in delete_list:
            folder_path = os.path.join(report_dir, folder)
            try:
                shutil.rmtree(folder_path)
                print(f"✅ 已删除：{folder_path}")
            except Exception as e:
                print(f"⚠️ 删除失败：{folder_path}, 错误：{e}")
    else:
        print("报告数量未超出限制，无需清理。")


import os


def clear_logs_keep_n(keep,folder_name):
    """
    清理指定日志目录中以 log.log 开头的日志文件，只保留最新 keep 个。

    :param folder_name: 日志目录名（相对于项目根目录，如 "testLog"）
    :param keep: 要保留的日志数量（默认保留 5 个）
    """
    # 构造完整路径：项目根目录 + 日志文件夹
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), folder_name)

    if not os.path.exists(log_dir):
        print(f"❌ 日志目录不存在：{log_dir}")
        return

    # 筛选所有以 log.log 开头的文件（包含 log.log 和 log.log.202x）
    log_files = [
        f for f in os.listdir(log_dir)
        if os.path.isfile(os.path.join(log_dir, f)) and f.startswith("log.log")
    ]

    # 按最后修改时间排序，旧的在前
    log_files.sort(key=lambda f: os.path.getmtime(os.path.join(log_dir, f)))

    if len(log_files) > keep:
        delete_list = log_files[:len(log_files) - keep]
        print(f"🧹 清理日志目录 {folder_name}，保留最新 {keep} 个：")
        for file in delete_list:
            file_path = os.path.join(log_dir, file)
            try:
                os.remove(file_path)
                print(f"✅ 删除日志：{file}")
            except Exception as e:
                print(f"⚠️ 删除失败：{file}，原因：{e}")
    else:
        print(f"📦 当前日志数量 {len(log_files)}，未超过 {keep} 个，无需清理。")


if __name__ == '__main__':
    # autoClear(5, "testLog")
    clear_logs_keep_n(10,"testLog")
