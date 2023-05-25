from pydantic import BaseSettings



class Settings(BaseSettings):
    motors_port: str

    class Config:
        env_file = '.env'

settings = Settings()