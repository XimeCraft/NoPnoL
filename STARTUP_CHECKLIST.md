# NoPnoL 完整启动清单

## 从零开始的启动步骤

### ✅ Checklist

```bash
# ========================================
# 1. 进入项目目录
# ========================================
cd /Users/xiao/Projects/git/NoPnoL


# ========================================
# 2. 清理所有旧进程（重要！）
# ========================================
lsof -ti:8000 | xargs kill -9 2>/dev/null
lsof -ti:3000 | xargs kill -9 2>/dev/null
lsof -ti:3001 | xargs kill -9 2>/dev/null


# ========================================
# 3. 删除旧数据库并重新初始化（重要！）
# ========================================
cd /Users/xiao/Projects/git/NoPnoL
rm -f nopnol.db
/Users/xiao/Projects/git/NoPnoL/venv/bin/python3 backend/init_db.py


# ========================================
# 4. 验证数据库（可选，但推荐）
# ========================================
/Users/xiao/Projects/git/NoPnoL/venv/bin/python3 << 'EOF'
from backend.database import SessionLocal
from backend.models import Category, Article

db = SessionLocal()
print(f'✅ Categories: {db.query(Category).count()}')
print(f'✅ Articles: {db.query(Article).count()}')
db.close()
EOF


# ========================================
# 5. 启动后端（在当前终端）
# ========================================
/Users/xiao/Projects/git/NoPnoL/venv/bin/uvicorn backend.main:app --reload

# ⏸️ 等待看到: "Application startup complete."
# 不要关闭这个终端！


# ========================================
# 6. 验证后端 API（打开新终端）
# ========================================
# 在新终端中运行：
curl http://localhost:8000/api/categories
curl http://localhost:8000/api/articles

# 应该看到 JSON 数据，不是 "detail": "Not Found"


# ========================================
# 7. 启动前端（在另一个新终端）
# ========================================
cd /Users/xiao/Projects/git/NoPnoL/frontend
npm run dev

# ⏸️ 等待看到: "Local: http://localhost:3001/"


# ========================================
# 8. 访问应用
# ========================================
# 浏览器打开: http://localhost:3001
# 强制刷新: Cmd + Shift + R
```

---

## 简化版（复制粘贴使用）

### 终端 1 - 启动后端

```bash
cd /Users/xiao/Projects/git/NoPnoL
lsof -ti:8000 | xargs kill -9 2>/dev/null
rm -f nopnol.db
/Users/xiao/Projects/git/NoPnoL/venv/bin/python3 backend/init_db.py
/Users/xiao/Projects/git/NoPnoL/venv/bin/uvicorn backend.main:app --reload
```

### 终端 2 - 验证并启动前端

```bash
# 等待后端启动完成（看到 "Application startup complete."）

# 验证后端
curl http://localhost:8000/api/categories
curl http://localhost:8000/api/articles

# 如果上面返回正常 JSON，启动前端
cd /Users/xiao/Projects/git/NoPnoL/frontend
lsof -ti:3001 | xargs kill -9 2>/dev/null
npm run dev
```

---

## 故障排查

### 问题：API 返回 404

**可能原因 1：数据库文件损坏或缺失**

```bash
# 删除旧数据库
cd /Users/xiao/Projects/git/NoPnoL
rm nopnol.db

# 重新初始化
/Users/xiao/Projects/git/NoPnoL/venv/bin/python3 backend/init_db.py

# 重启后端
lsof -ti:8000 | xargs kill -9
/Users/xiao/Projects/git/NoPnoL/venv/bin/uvicorn backend.main:app --reload
```

**可能原因 2：虚拟环境问题**

```bash
# 检查虚拟环境是否存在
ls -la /Users/xiao/Projects/git/NoPnoL/venv/bin/

# 如果不存在，重新创建虚拟环境
cd /Users/xiao/Projects/git/NoPnoL
python3 -m venv venv
/Users/xiao/Projects/git/NoPnoL/venv/bin/pip install -r requirements.txt
```

**可能原因 3：检查后端日志**

在后端终端查看错误信息，特别注意：
- `ModuleNotFoundError` - 依赖未安装
- `Table doesn't exist` - 数据库未初始化
- `Address already in use` - 端口被占用

### 问题：前端白屏或 items 不显示

```bash
# 1. 检查后端是否真的在运行
curl http://localhost:8000/api/categories

# 2. 检查浏览器控制台（F12）
# 查看是否有 CORS 错误或网络错误

# 3. 检查前端端口
lsof -ti:3001

# 4. 强制刷新浏览器
# Cmd + Shift + R (Mac) 或 Ctrl + Shift + R (Windows/Linux)
```

---

## 快速一键启动脚本（推荐）

创建文件 `quick_start.sh`:

```bash
#!/bin/bash

echo "🚀 NoPnoL 快速启动脚本"
echo ""

cd /Users/xiao/Projects/git/NoPnoL

echo "1️⃣  清理旧进程..."
lsof -ti:8000 | xargs kill -9 2>/dev/null
lsof -ti:3000 | xargs kill -9 2>/dev/null
lsof -ti:3001 | xargs kill -9 2>/dev/null
sleep 1

echo "2️⃣  初始化数据库..."
/Users/xiao/Projects/git/NoPnoL/venv/bin/python3 backend/init_db.py

echo "3️⃣  启动后端..."
/Users/xiao/Projects/git/NoPnoL/venv/bin/uvicorn backend.main:app --reload &
BACKEND_PID=$!
sleep 3

echo "4️⃣  验证后端..."
if curl -s http://localhost:8000/api/categories | grep -q "id"; then
    echo "✅ 后端正常"
    CATEGORIES=$(curl -s http://localhost:8000/api/categories | python3 -c "import sys, json; print(len(json.load(sys.stdin)))")
    ARTICLES=$(curl -s http://localhost:8000/api/articles | python3 -c "import sys, json; print(len(json.load(sys.stdin)))")
    echo "   - Categories: $CATEGORIES"
    echo "   - Articles: $ARTICLES"
else
    echo "❌ 后端启动失败"
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

echo "5️⃣  启动前端..."
cd frontend
npm run dev &
FRONTEND_PID=$!

echo ""
echo "════════════════════════════════════════"
echo "  ✅ 启动完成！"
echo "════════════════════════════════════════"
echo ""
echo "  后端: http://localhost:8000"
echo "  API: http://localhost:8000/docs"
echo "  前端: http://localhost:3001"
echo ""
echo "  按 Ctrl+C 停止所有服务"
echo ""

# 等待用户中断
trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT
wait
```

使用方法：

```bash
# 赋予执行权限
chmod +x quick_start.sh

# 运行
./quick_start.sh
```

---

## 每天工作流程建议

1. **早上开始工作：**
   ```bash
   ./quick_start.sh
   ```

2. **修改代码时：**
   - 后端会自动重载（uvicorn --reload）
   - 前端会自动热更新（Vite HMR）
   - 无需重启

3. **遇到问题时：**
   - Ctrl+C 停止脚本
   - 重新运行 `./quick_start.sh`

4. **下班前：**
   - Ctrl+C 停止所有服务
