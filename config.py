from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AquaPod API",
    admin_email: str = "luka.blaskovic@student.unipu.hr"
