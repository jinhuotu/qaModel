# 项目目录
    qaModel/
    ├── app/
    │   ├── routers/                # FastAPI 路由层（API 入口）
    │   │   ├── upload_router.py    # 文件上传相关接口
    │   │   ├── query_router.py     # 问答相关接口
    │   │   └── __init__.py
    │   ├── schemas/               # Pydantic 数据模型定义
    │   │   ├── upload.py          # 文件上传请求模型
    │   │   ├── query.py           # 问答请求/响应模型
    │   │   └── __init__.py
    │   ├── services/              # 核心业务逻辑层
    │   │   ├── document_processing/  # 文档处理模块
    │   │   │   ├── file_parser.py    # 文件解析（PDF/TXT/DOCX）
    │   │   │   ├── text_splitter.py  # 文本切分逻辑
    │   │   │   └── __init__.py
    │   │   ├── retrieval/         # 检索模块
    │   │   │   ├── vector_db.py   # 向量数据库操作（Chroma/FAISS）
    │   │   │   └── __init__.py
    │   │   ├── analysis/          # 分析模块
    │   │   │   ├── local_llm.py   # 本地模型处理
    │   │   │   ├── deepseek.py    # DeepSeek 接口封装
    │   │   │   └── __init__.py
    │   │   └── __init__.py
    │   ├── models/                # 数据库模型（SQLAlchemy ORM）
    │   │   ├── document_model.py  # 文档存储元数据
    │   │   └── __init__.py
    │   ├── core/                  # 核心配置和工具
    │   │   ├── config.py          # 全局配置（环境变量加载）
    │   │   ├── dependencies.py    # 依赖注入（如数据库连接）
    │   │   ├── exceptions.py      # 自定义异常处理
    │   │   └── __init__.py
    │   ├── utils/                 # 通用工具函数
    │   │   ├── logger.py          # 日志配置
    │   │   ├── storage.py         # 文件存储工具
    │   │   └── __init__.py
    │   ├── db/                    # 数据库管理
    │   │   ├── session.py         # 数据库会话管理
    │   │   └── __init__.py
    │   └── main.py                # FastAPI 应用初始化
    ├── data/                      # 数据存储（建议添加到.gitignore）
    │   ├── uploaded_files/        # 原始文档存储（按用户ID分目录）
    │   ├── processed_chunks/      # 处理后的文本块（JSON格式）
    │   └── vector_storage/        # 向量数据库持久化数据
    ├── tests/                     # 测试目录
    │   ├── unit/                  # 单元测试
    │   └── integration/           # 集成测试
    ├── scripts/                   # 实用脚本
    │   ├── migrate_db.py          # 数据库迁移脚本
    │   └── cleanup_storage.py     # 存储清理脚本
    ├── requirements/
    │   ├── base.txt               # 基础依赖
    │   ├── dev.txt                # 开发依赖
    │   └── prod.txt               # 生产依赖
    ├── Dockerfile
    ├── docker-compose.yml
    ├── .env.template              # 环境变量模板
    └── README.md

### 全局日志使用方法

    from app.utils.logger import logger
    
    logger.debug("Debug detail", extra={"user_id": 123})
    logger.warning("Unusual event", extra={"ip": "192.168.1.1"})
