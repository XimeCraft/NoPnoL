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
# 删除旧数据库确保干净启动
rm -f nopnol.db
/Users/xiao/Projects/git/NoPnoL/venv/bin/python3 backend/init_db.py

echo "3️⃣  启动后端..."
/Users/xiao/Projects/git/NoPnoL/venv/bin/uvicorn backend.main:app --reload &
BACKEND_PID=$!
sleep 3

echo "4️⃣  验证后端..."
if curl -s http://localhost:8000/api/categories | grep -q "id"; then
    echo "✅ 后端正常"
    CATEGORIES=$(curl -s http://localhost:8000/api/categories | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null || echo "0")
    ARTICLES=$(curl -s http://localhost:8000/api/articles | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null || echo "0")
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
