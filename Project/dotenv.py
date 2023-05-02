import pydantic
from pydantic import BaseSettings

class Settings(BaseSettings):
    host:str
    database:str
    user:str
    password:str
    class Config:
        env_file = "C:\\Users\\HP PC\\Desktop\\Beast_backend\\SQL\\.env"
        
Process = Settings()


        
    
    