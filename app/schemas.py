from pydantic import BaseModel


class AquaPod(BaseModel):
    ime: str


class Unit(BaseModel):
    name: str
    symbol: str
    description: str


class VideoCamera(BaseModel):
    is_on: bool = False
    pan: float
    zoom: float


class GPSPosition(BaseModel):
    latitude: float
    longitude: float


class TrashContainer(BaseModel):
    garbage_filled: float


class Pump(BaseModel):
    speed: int
    working_time: float
    alarm_status: str


class Battery(BaseModel):
    charge_current: float
    discharge_current: float
    voltage: float
    capacity: float
    cycle_count: int


class SolarPanel(BaseModel):
    insolation: float
    voltage: float
    utilization: float
    working_time: float


class Environment(BaseModel):
    sea_depth: float
    sea_temperature: float
    sea_ph: float
    wind_direction: float
    wind_power: float
    air_temperature: float


class PumpAudit(BaseModel):
    speed: int
    working_time: float
    alarm_status: str


class BatteryAudit(BaseModel):
    charge_current: float
    discharge_current: float
    voltage: float
    capacity: float
    cycle_count: int


class SolarPanelAudit(BaseModel):
    insolation: float
    voltage: float
    utilization: float
    working_time: float


class EnvironmentAudit(BaseModel):
    sea_depth: float
    sea_temperature: float
    sea_ph: float
    wind_direction: float
    wind_power: float
    air_temperature: float
