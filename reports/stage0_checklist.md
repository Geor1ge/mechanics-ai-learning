# Learning Log

## 2026-06-03：第0阶段 - 工具链与科研编程环境

### 今日完成

- 已在 Windows 上准备 Anaconda、PyCharm、Jupyter、VS Code 等工具。
- 已在 WSL Ubuntu 中建立本地项目路径：

```text
~/projects/mechanics-ai-learning
- 已创建 GitHub 远程仓库：
https://github.com/Geor1ge/mechanics-ai-learning

- 已理解以下概念区别：
WSL Ubuntu：Linux 开发环境
mechanics-ai-learning：本地项目文件夹 / 本地 Git 仓库
GitHub mechanics-ai-learning：远程代码仓库
mechanics-ai：conda Python 环境

- 已安装或准备安装 Miniforge。
- 已创建 mechanics-ai conda 环境。
- 已建立基础项目结构：
    src/
    notebooks/
    scripts/
    data/
    results/
    tests/
    reports/
    docs/

- 今日重点理解
    1.apt 用于安装 Ubuntu 系统工具，例如 git、curl、tree。
    2.conda 用于管理 Python 环境和科学计算包。
    3.environment.yml 是环境配置说明书。
    4.mechanics-ai 是根据 environment.yml 创建出来的实际 Python 环境。
    5.git commit 是保存到本地 Git 历史。
    6.git push 是上传到 GitHub 远程仓库。

- 遇到的问题
    1.初次 git commit 时出现作者身份未配置问题。
    2.初次 git push 时出现远程仓库已有提交，需要先 git pull。
    3.对本地仓库、GitHub 仓库、conda 环境的路径关系一开始有混淆，目前已基本理清。

- 下一步计划
    1.完成 .gitignore、README.md、environment.yml、test_environment.py 的编辑。
    2.运行环境测试脚本。
    3.运行 pytest 测试。
    4.完成一次规范 Git 提交。
    5.推送到 GitHub。


---

### 第0阶段检查表

## 1. 软件与环境

- [x] Windows 已安装 Anaconda
- [x] Windows 已安装 PyCharm
- [x] Windows 已安装 Jupyter
- [x] Windows 已安装 VS Code
- [x] WSL Ubuntu 可用
- [x] 已创建本地项目目录
- [x] 已创建 GitHub 远程仓库
- [x] 已安装 Miniforge
- [x] 已创建 mechanics-ai conda 环境
- [x] 已完成环境测试脚本运行

## 2. Linux 命令

已熟悉：

- [x] cd
- [x] ls
- [x] grep
- [x] find
- [x] ssh
- [x] scp
- [x] tmux

需要继续熟悉：

- [ ] pwd
- [ ] mkdir
- [ ] rm
- [ ] cp
- [ ] mv
- [ ] cat
- [ ] head
- [ ] tail
- [ ] less
- [ ] chmod
- [ ] tree
- [ ] htop
- [ ] rsync

## 3. Git 与 GitHub

- [x] 已创建本地仓库
- [x] 已创建 GitHub 远程仓库
- [x] 已配置 Git user.name
- [x] 已配置 Git user.email
- [x] 已完成第一次 commit
- [x] 已完成第一次 push
- [x] 能解释 git add / commit / push / pull 的区别

## 4. 项目结构

- [x] README.md
- [x] LICENSE
- [x] environment.yml
- [x] src/
- [x] notebooks/
- [x] scripts/
- [x] data/
- [x] results/
- [x] tests/
- [x] reports/
- [x] docs/
- [x] .gitignore
- [x] notebooks/README.md

## 5. 第0阶段达标标准

完成以下任务后，第0阶段可以认为基本达标：

- 能进入项目目录：
    cd ~/projects/mechanics-ai-learning
- 能激活 conda 环境：
    conda activate mechanics-ai
- 能运行环境测试：
    python scripts/test_environment.py
- 能运行测试：
    PYTHONPATH=src pytest
- 能完成 Git 提交流程：
    git status
    git add .
    git commit -m "message"
    git push

- 下一阶段准备，第1阶段将进入 Python 科研编程，包括：
    1.Python 基础语法
    2.NumPy 数组计算
    3.Matplotlib 科研绘图
    4.Pandas 数据处理
    5.一维 Poisson / Heat Equation 数值求解

## 6. 运行检查提交到 GitHub
依次执行：
python scripts/test_environment.py
PYTHONPATH=src pytest
tree -a -I ".git|__pycache__|.pytest_cache|.ipynb_checkpoints"
git status
git add .
git commit -m "Update stage 0 project structure and environment files"
如果你前面远程仓库有 README 导致冲突，先执行：git pull origin main --allow-unrelated-histories
如果没有冲突，再推送：git push -u origin main












## 软件安装

- [ ] Anaconda
- [ ] VS Code
- [ ] Git
- [ ] JupyterLab
- [ ] PyCharm
- [ ] WSL2 Ubuntu，可选

## 命令行

- [ ] cd / ls / pwd
- [ ] grep / find
- [ ] ssh / scp
- [ ] tmux
- [ ] git status / add / commit / push

## 仓库结构

- [ ] README.md
- [ ] environment.yml
- [ ] .gitignore
- [ ] src/
- [ ] notebooks/
- [ ] scripts/
- [ ] data/
- [ ] results/
- [ ] tests/
- [ ] reports/
- [ ] docs/

## 当前问题

## 下阶段计划
