from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
# Schema/Pydantic model defines the structure of a request & response

# AQUAPOD


class AquaPodBase(BaseModel):
    name: str


class AquaPodCreate(AquaPodBase):
    pass


class Aquapod(AquaPodBase):
    id: int

    class Config:
        orm_mode = True


class AquaPodWithLatestData(AquaPodBase):
    id: int
    latest_data: list

    class Config:
        orm_mode = True

# VIDEO CAMERA


class VideoCameraCreate(BaseModel):
    aquapod_id: int
    is_on: bool = False
    pan: float = 0.0
    zoom: float = 0.0
    operational_timestamp: datetime


class VideoCamera(VideoCameraCreate):
    id: int

    class Config:
        orm_mode = True

# GPS POSITION


class GPSPositionCreate(BaseModel):
    aquapod_id: Optional[int] = None
    latitude: float = 0.0
    longitude: float = 0.0
    operational_timestamp: Optional[datetime] = None


class GPSPosition(GPSPositionCreate):
    id: int
    latitude_unit_id: int
    longitude_unit_id: int

    class Config:
        orm_mode = True

# TRASH CONTAINER


class TrashContainerCreate(BaseModel):
    aquapod_id: Optional[int] = None
    garbage_filled: float = 0.0
    operational_timestamp: Optional[datetime] = None


class TrashContainer(TrashContainerCreate):
    id: int

    class Config:
        orm_mode = True

# PUMP


class PumpCreate(BaseModel):
    aquapod_id: Optional[int] = None
    speed: int = 0
    working_time: float = 0.0
    alarm_status: Optional[str] = None
    operational_timestamp: Optional[datetime] = None


class Pump(PumpCreate):
    id: int
    speed_unit_id: int

    class Config:
        orm_mode = True

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
    charge_current_unit_id: int
    discharge_current_unit_id: int
    voltage_unit_id: int
    capacity_unit_id: int

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
    insolation_unit_id: int
    voltage_unit_id: int
    utilization_unit_id: int

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
    sea_depth_unit_id: int
    sea_temperature_unit_id: int
    sea_ph_unit_id: int
    wind_direction_unit_id: int
    wind_power_unit_id: int
    air_temperature_unit_id: int

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
