from fastapi import APIRouter, UploadFile, HTTPException, status
from pathlib import Path
from app.utils.logger import configure_logging
from app.core.config import settings
from app.services.document_processing.file_parser import parse_file
import logging

# ✅ 使用根日志器
configure_logging()
logger = logging.getLogger()
router = APIRouter(prefix="/upload", tags=["File Upload"])

ALLOWED_MIME_TYPES = {
    "text/plain": "txt",
    "application/pdf": "pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "docx"
}

logger.debug("=== 应用启动 ===")

@router.post("", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile):
    # 验证文件类型
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file type: {file.content_type}"
        )

    try:
        # 创建存储目录
        upload_dir = Path(settings.UPLOAD_DIR)
        upload_dir.mkdir(parents=True, exist_ok=True)

        # 解析文件内容
        content = await parse_file(file)

        # 保存原始文件
        file_path = upload_dir / file.filename
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        logger.info("File uploaded successfully", extra={
            "filename": file.filename,
            "size": file.size,
            "saved_path": str(file_path)
        })

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "size": file.size,
            "content_length": len(content)
        }

    except Exception as e:
        logger.error("File upload failed", exc_info=True, extra={
            "error": str(e),
            "filename": file.filename
        })
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="File processing failed"
        )