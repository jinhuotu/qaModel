# app/main.py
from app.routers import upload_router
from app.utils.logger import configure_logging

# ✅ 第一步：初始化日志（必须在所有导入之前）
configure_logging()

from fastapi import FastAPI
import logging

# ✅ 使用根日志器
logger = logging.getLogger()
app = FastAPI()

app.include_router(upload_router.router, prefix="/api/v1/files")
@app.get("/")
def read_root():
    logger.debug("=== 应用启动2 ===")
    logger.info("Root endpoint called")
    return {"message": "API is running!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_config=None,  # ✅ 禁用Uvicorn默认配置
        access_log=False  # ✅ 关闭访问日志避免干扰
    )
