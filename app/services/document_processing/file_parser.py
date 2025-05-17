from typing import Union
import io
from fastapi import UploadFile
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
from app.utils.logger import configure_logging
import logging
configure_logging()
logger = logging.getLogger()


async def parse_file(file: UploadFile) -> str:
    content = await file.read()

    try:
        if file.content_type == "application/pdf":
            return extract_pdf_text(io.BytesIO(content))

        elif file.content_type == "text/plain":
            return content.decode("utf-8")

        elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(io.BytesIO(content))
            return "\n".join([para.text for para in doc.paragraphs])

        else:
            raise ValueError(f"Unsupported file type: {file.content_type}")

    except Exception as e:
        logger.error("File parsing failed", exc_info=True, extra={
            "filename": file.filename,
            "error": str(e)
        })
        raise