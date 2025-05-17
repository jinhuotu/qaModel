from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # 应用配置
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = False

    # 文件存储路径
    UPLOAD_DIR: Path = Path("data/uploaded_files")
    PROCESSED_DIR: Path = Path("data/processed_chunks")

    # 向量数据库配置
    VECTOR_DB_PATH: Path = Path("data/vector_storage/chroma")
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"

    # DeepSeek API 配置
    DEEPSEEK_API_KEY: str = ""
    DEEPSEEK_API_BASE: str = "https://api.deepseek.com/v1"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()