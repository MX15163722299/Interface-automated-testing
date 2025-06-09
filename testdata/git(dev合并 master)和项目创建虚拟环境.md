### 一. dev合并master分支

git checkout master
git pull origin master
git merge dev
git push origin master



### 二. 将依赖下载到 requirements.txt文件中

pip freeze > requirements.txt



### 三. 创建虚拟环境，安装依赖

## 场景：刚从 Git 下载了代码，没有环境，怎么办？

### 🎯 目标：

创建一个虚拟环境 → 安装依赖 → 顺利运行代码

------

## 🚀 Step-by-Step 操作指南（适用于 Windows / macOS / Linux）

------

### 🧱 1. 打开终端 / CMD，进入项目目录

```
bash


复制编辑
cd your_project_folder/
```

------

### 🐍 2. 创建虚拟环境 `.venv`

```
bash复制编辑# Windows
python -m venv .venv

# macOS / Linux
python3 -m venv .venv
```

这会在当前项目目录下创建一个 `.venv` 文件夹，专门用于当前项目的独立环境。

------

### ✅ 3. 激活虚拟环境

```
bash复制编辑# Windows
.\.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

激活后，终端前面一般会看到 `(.venv)`，说明环境生效了。

------

### 📦 4. 安装项目依赖

假设项目目录里有 `requirements.txt`：

```
bash


复制编辑
pip install -r requirements.txt
```

🔸 如果没有 `requirements.txt`，那就你自己手动装，或看文档说明：

```
bash


复制编辑
pip install flask requests pytest openpyxl ...
```

------

### 🧪 5. 运行代码 / 测试是否正常

```
bash复制编辑# 比如运行 main 文件
python main.py

# 或运行测试
pytest
```

------

## 📌 一句话总结流程：

```
bash复制编辑cd 项目目录
python -m venv .venv
.\.venv\Scripts\activate    # 或 source .venv/bin/activate
pip install -r requirements.txt
python main.py 或 pytest
```

------

## 🛑 注意事项

| 问题                    | 说明                                                         |
| ----------------------- | ------------------------------------------------------------ |
| `python` 不是内部命令   | 说明 Python 没安装或没加环境变量                             |
| 没有 `requirements.txt` | 可以请作者提供，或你跑一遍后再用 `pip freeze > requirements.txt` 自己生成 |
| 模块缺失错误            | 用 `pip install 模块名` 安装它                               |