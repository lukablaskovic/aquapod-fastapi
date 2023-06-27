from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from .db import Base

# Schalchemy model - defines what our database looks like, as well as ORM relationships


class AquaPod(Base):
    __tablename__ = "aquapod"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    total_garbage_collected = Column(Float, nullable=False, default=0.0)

    video_camera = relationship(
        "VideoCamera", back_populates="aquapod")
    gps_position = relationship(
        "GPSPosition", back_populates="aquapod")
    trash_container = relationship(
        "TrashContainer", back_populates="aquapod")
    pump = relationship(
        "Pump", back_populates="aquapod")
    battery = relationship(
        "Battery", back_populates="aquapod")
    solar_panel = relationship(
        "SolarPanel", back_populates="aquapod")
    environment = relationship(
        "Environment", back_populates="aquapod")


class Unit(Base):
    __tablename__ = "unit"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    symbol = Column(String, nullable=False)
    description = Column(String)

# General


class VideoCamera(Base):
    __tablename__ = "video_camera"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"))
    aquapod = relationship("AquaPod", back_populates="video_camera")

    status = Column(Boolean, nullable=False, default=False)
    pan = Column(Float, nullable=False, default=0.0)
    zoom = Column(Float, nullable=False, default=0.0)

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class GPSPosition(Base):
    __tablename__ = "gps_position"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"))
    aquapod = relationship(
        "AquaPod", back_populates="gps_position", uselist=False)

    latitude = Column(Float, nullable=False, default=0.0)
    longitude = Column(Float, nullable=False, default=0.0)

    latitude_unit_id = Column(Integer, ForeignKey(
        "unit.id"), default=11)  # degree °
    longitude_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=11)  # degree °

    latitude_unit = relationship(
        "Unit", foreign_keys=[latitude_unit_id])
    longitude_unit = relationship(
        "Unit", foreign_keys=[longitude_unit_id])

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class TrashContainer(Base):
    __tablename__ = "trash_container"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"))
    container_filled = Column(Float, nullable=False, default=0.0)
    container_capacity = Column(Float, nullable=False, default=0.0)

    container_filled_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=14)  # gram g

    container_capacity_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=14)  # gram g

    container_filled_unit = relationship(
        "Unit", foreign_keys=[container_filled_unit_id])

    container_capacity_unit = relationship(
        "Unit", foreign_keys=[container_capacity_unit_id])

    alarm_status = Column(Boolean, nullable=False, default=False)
    garbage_collected_total = Column(Float, nullable=False, default=0.0)
    emptying = Column(Boolean, nullable=False, default=False)
    aquapod = relationship(
        "AquaPod", back_populates="trash_container", uselist=False)

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


# Components

class Pump(Base):
    __tablename__ = "pump"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"))
    aquapod = relationship("AquaPod", back_populates="pump", uselist=False)

    speed = Column(Integer, nullable=False, default=0.0)
    status = Column(Boolean, nullable=False, default=False)
    working_time = Column(Float, nullable=False, default=0.0)
    alarm_status = Column(String)

    speed_unit_id = Column(Integer, ForeignKey("unit.id"), default=1)  # RPM
    speed_unit = relationship(
        "Unit", foreign_keys=[speed_unit_id])

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class Battery(Base):
    __tablename__ = "battery"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"))
    aquapod = relationship(
        "AquaPod", back_populates="battery", uselist=False)

    charge_current = Column(Float, nullable=False, default=0.0)
    discharge_current = Column(Float, nullable=False, default=0.0)
    voltage = Column(Float, nullable=False, default=0.0)
    capacity = Column(Float, nullable=False, default=0.0)
    cycle_count = Column(Integer, nullable=False, default=0)

    charge_current_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=2)  # A
    discharge_current_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=2)  # A
    voltage_unit_id = Column(Integer, ForeignKey("unit.id"), default=3)  # V
    capacity_unit_id = Column(Integer, ForeignKey("unit.id"), default=4)  # Ah

    charge_current_unit = relationship(
        "Unit", foreign_keys=[charge_current_unit_id])
    discharge_current_unit = relationship(
        "Unit", foreign_keys=[discharge_current_unit_id])
    voltage_unit = relationship(
        "Unit", foreign_keys=[voltage_unit_id])
    capacity_unit = relationship(
        "Unit", foreign_keys=[capacity_unit_id])

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class SolarPanel(Base):
    __tablename__ = "solar_panel"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"))
    aquapod = relationship(
        "AquaPod", back_populates="solar_panel", uselist=False)

    insolation = Column(Float, nullable=False, default=0.0)
    voltage = Column(Float, nullable=False, default=0.0)
    utilization = Column(Float, nullable=False, default=0.0)
    working_time = Column(Float, nullable=False, default=0.0)

    insolation_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=6)  # kWh/m2
    voltage_unit_id = Column(Integer, ForeignKey("unit.id"), default=3)  # V
    utilization_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=7)  # W

    insolation_unit = relationship(
        "Unit", foreign_keys=[insolation_unit_id])
    voltage_unit = relationship(
        "Unit", foreign_keys=[voltage_unit_id])
    utilization_unit = relationship(
        "Unit", foreign_keys=[utilization_unit_id])

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))

# Sensor data


class Environment(Base):
    __tablename__ = "environment"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"))
    aquapod = relationship(
        "AquaPod", back_populates="environment", uselist=False)

    sea_depth = Column(Float, nullable=False, default=0.0)
    sea_temperature = Column(Float, nullable=False, default=0.0)
    sea_ph = Column(Float, nullable=False, default=0.0)
    wind_direction = Column(Float, nullable=False, default=0.0)
    wind_power = Column(Float, nullable=False, default=0.0)
    air_temperature = Column(Float, nullable=False, default=0.0)

    sea_depth_unit_id = Column(Integer, ForeignKey("unit.id"), default=8)  # m
    sea_temperature_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=9)  # °C
    sea_ph_unit_id = Column(Integer, ForeignKey("unit.id"), default=10)  # pH
    wind_direction_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=11)  # degree °
    wind_power_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=12)  # km/h
    air_temperature_unit_id = Column(
        Integer, ForeignKey("unit.id"), default=9)  # °C

    sea_depth_unit = relationship(
        "Unit", foreign_keys=[sea_depth_unit_id])
    sea_temperature_unit = relationship(
        "Unit", foreign_keys=[sea_temperature_unit_id])
    sea_ph_unit = relationship(
        "Unit", foreign_keys=[sea_ph_unit_id])
    wind_direction_unit = relationship(
        "Unit", foreign_keys=[wind_direction_unit_id])
    wind_power_unit = relationship(
        "Unit", foreign_keys=[wind_power_unit_id])
    air_temperature_unit = relationship(
        "Unit", foreign_keys=[air_temperature_unit_id])

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

# Drop all tables
# DROP SCHEMA public CASCADE
# CREATE SCHEMA public
