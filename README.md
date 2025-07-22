# BaZi Calculator (八字计算器)

以寿星天文历为基础，封装为标准八字排盘、用神推断的Python项目。

## 功能特性

1. 封装天干、地支、四柱、十神、五行旺衰计算
2. 封装规则库：支持天干五合、冲、克、地支的刑冲合害、三会、三合判断
3. 提供标准的Python包结构，便于安装和使用

## 安装说明

### 方法一：直接运行
```bash
# 克隆或下载项目
cd /path/to/bazi-calculator

# 安装依赖（如果有）
pip install -r requirements.txt

# 运行程序
python main.py
```

### 方法二：开发模式安装
```bash
# 开发模式安装
pip install -e .

# 运行命令行工具
bazi-calc

# 或者直接运行
python main.py
```

### 方法三：构建并安装
```bash
# 安装构建工具
pip install build

# 构建包
python -m build

# 安装构建的包
pip install dist/bazi_calculator-1.0.0-py3-none-any.whl
```

## 使用说明

### 命令行使用
```bash
# 运行默认示例
python main.py

# 或使用安装的命令
bazi-calc
```

### 编程接口
```python
from BZPaipan import BzPaipan
from BzRules import Bzrules

# 创建排盘实例
paipan = BzPaipan()

# 阳历排盘 (年, 月, 日, 时)
bzyj = paipan.getPaipanbySun(2002, 12, 25, 8)
bzyj.getPaiPan()

# 获取各种关系
print("天干合：", Bzrules.getTgHeshiResult(bzyj.tglist))
print("天干冲：", Bzrules.getTgChongResult(bzyj.tglist))
print("地支合：", Bzrules.getZhiHeResult(bzyj.zhilist))
print("地支冲：", Bzrules.getZhiChoneResult(bzyj.zhilist))
```

## 开发说明

### 运行测试
```bash
# 安装测试依赖
pip install pytest

# 运行测试
python -m pytest tests/ -v

# 或使用Makefile
make test
```

### 开发命令
```bash
# 查看所有可用命令
make help

# 构建包
make build

# 安装开发依赖
make requirements

# 清理构建文件
make clean
```

## 项目结构
```
bazi-calculator/
├── main.py              # 主入口文件
├── __init__.py          # 包初始化文件
├── BZPaipan.py         # 排盘核心类
├── BzRules.py          # 规则库
├── BzBaseClass.py      # 基础类
├── BZBaseTools.py      # 基础工具
├── StaticDict.py       # 静态字典
├── requirements.txt    # 依赖列表
├── setup.py           # 安装脚本
├── pyproject.toml     # 现代构建配置
├── Makefile           # 开发命令
├── tests/             # 测试目录
└── README.md          # 说明文档
```

## 许可证

MIT License - 详见 LICENSE 文件
