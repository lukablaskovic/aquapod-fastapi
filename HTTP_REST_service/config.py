from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AquaPod HTTP REST-API",
    admin_email: str = "luka.blaskovic@student.unipu.hr"
