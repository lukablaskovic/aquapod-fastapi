from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
# Schema/Pydantic model defines the structure of a request & response

# AQUAPOD


class AquaPodBase(BaseModel):
    name: str
    total_garbage_collected: float = 0.0


class AquaPodCreate(AquaPodBase):
    pass


class Aquapod(AquaPodBase):
    id: int

    class Config:
        orm_mode = True


class AquaPodPublic(AquaPodBase):
    environment: list


class AquaPodWithLatestData(AquaPodBase):
    id: int
    latest_data: list

    class Config:
        orm_mode = True


# UNIT


class Unit(BaseModel):
    id: int
    name: str
    symbol: str
    description: str

    class Config:
        orm_mode = True


# VIDEO CAMERA


class VideoCameraCreate(BaseModel):
    aquapod_id: Optional[int] = None
    status: bool = False
    pan: float = 0.0
    zoom: float = 0.0
    operational_timestamp: Optional[datetime] = None


class VideoCamera(VideoCameraCreate):
    id: int

    class Config:
        orm_mode = True


class VideoCameraUpdate(BaseModel):
    status: Optional[bool] = None
    pan: Optional[float] = None
    zoom: Optional[float] = None


# GPS POSITION


class GPSPositionCreate(BaseModel):
    aquapod_id: Optional[int] = None
    latitude: float = 0.0
    longitude: float = 0.0
    operational_timestamp: Optional[datetime] = None


class GPSPosition(BaseModel):
    id: int
    aquapod_id: Optional[int] = None
    latitude: float = 0.0
    longitude: float = 0.0
    operational_timestamp: Optional[datetime] = None
    latitude_unit: Optional[Unit] = None
    longitude_unit: Optional[Unit] = None

    class Config:
        orm_mode = True

# TRASH CONTAINER


class TrashContainerCreate(BaseModel):
    aquapod_id: Optional[int] = None
    container_filled: float = 0.0
    container_capacity: float = 0.0
    alarm_status: Optional[bool] = False
    emptying: Optional[bool] = False
    operational_timestamp: Optional[datetime] = None


class TrashContainer(TrashContainerCreate):
    id: int
    container_filled_unit: Optional[Unit] = None
    container_capacity_unit: Optional[Unit] = None

    class Config:
        orm_mode = True

# PUMP


class PumpCreate(BaseModel):
    aquapod_id: Optional[int] = None
    speed: int = 0
    status: Optional[bool] = False
    working_time: float = 0.0
    alarm_status: Optional[str] = None
    operational_timestamp: Optional[datetime] = None


class Pump(PumpCreate):
    id: int
    speed_unit: Optional[Unit] = None

    class Config:
        orm_mode = True


class PumpUpdate(BaseModel):
    speed: Optional[int] = None
    status: Optional[bool] = None


# BATTERY


class BatteryCreate(BaseModel):
    aquapod_id: Optional[int] = None
    charge_current: float = 0.0
    discharge_current: float = 0.0
    voltage: float = 0.0
    capacity: float = 0.0
    cycle_count: int = 0
    operational_timestamp: Optional[datetime] = None


class Battery(BatteryCreate):
    id: int
    charge_current_unit: Optional[Unit] = None
    discharge_current_unit: Optional[Unit] = None
    voltage_unit: Optional[Unit] = None
    capacity_unit: Optional[Unit] = None

    class Config:
        orm_mode = True

# SOLAR PANEL


class SolarPanelCreate(BaseModel):
    aquapod_id: Optional[int] = None
    insolation: float = 0.0
    voltage: float = 0.0
    utilization: float = 0.0
    working_time: float = 0.0
    operational_timestamp: Optional[datetime] = None


class SolarPanel(SolarPanelCreate):
    id: int
    insolation_unit: Optional[Unit] = None
    voltage_unit: Optional[Unit] = None
    utilization_unit: Optional[Unit] = None

    class Config:
        orm_mode = True

# ENVIRONMENT


class EnvironmentCreate(BaseModel):
    aquapod_id: Optional[int] = None
    sea_depth: float = 0.0
    sea_temperature: float = 0.0
    sea_ph: float = 0.0
    wind_direction: float = 0.0
    wind_power: float = 0.0
    air_temperature: float = 0.0
    operational_timestamp: Optional[datetime] = None


class Environment(EnvironmentCreate):
    id: int
    sea_depth_unit: Optional[Unit] = None
    sea_temperature_unit: Optional[Unit] = None
    sea_ph_unit: Optional[Unit] = None
    wind_direction_unit: Optional[Unit] = None
    wind_power_unit: Optional[Unit] = None
    air_temperature_unit: Optional[Unit] = None

    class Config:
        orm_mode = True


# USER

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[str] = None
    user_email: Optional[EmailStr] = None
