from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AquaPod FastMQTT Client",
    admin_email: str = "luka.blaskovic@student.unipu.hr"
