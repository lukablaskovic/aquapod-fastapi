from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from .db import Base


class AquaPod(Base):
    __tablename__ = "aquapod"
    id = Column(Integer, primary_key=True, index=True)
    ime = Column(String, nullable=False)

    video_cam = relationship(
        "VideoCam", back_populates="aquapod", uselist=False)
    gps_position = relationship(
        "GPSPosition", back_populates="aquapod", uselist=False)
    kos_za_smece = relationship(
        "KosZaSmece", back_populates="aquapod", uselist=False)
    pumpa = relationship(
        "Pumpa", back_populates="aquapod", uselist=False)
    akumulator = relationship(
        "Akumulator", back_populates="aquapod", uselist=False)
    solarni_panel = relationship(
        "SolarniPanel", back_populates="aquapod", uselist=False)
    okolis = relationship(
        "Okolis", back_populates="aquapod", uselist=False)


class Unit(Base):
    __tablename__ = "unit"
    id = Column(Integer, primary_key=True, index=True)
    naziv = Column(String, nullable=False)
    kratica = Column(String, nullable=False)
    opis = Column(String)

# General


class VideoCam(Base):
    __tablename__ = "video_cam"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    aquapod = relationship("Aquapod", back_populates="video_cam")

    is_on = Column(Boolean, nullable=False)
    pan = Column(Float, nullable=False)
    zoom = Column(Float, nullable=False)


class GPSPosition(Base):
    __tablename__ = "gps_position"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    aquapod = relationship("Aquapod", back_populates="gps_position")

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    latitude_unit_id = Column(Integer, ForeignKey("unit.id"), unique=True)
    longitude_unit_id = Column(Integer, ForeignKey("unit.id"), unique=True)

    latitude_unit = relationship("Unit", foreign_keys=[latitude_unit_id])
    longitude_unit = relationship("Unit", foreign_keys=[longitude_unit_id])

    timestamp = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=text("NOW()"))


class KosZaSmece(Base):
    __tablename__ = "kos_za_smece"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    napunjenost = Column(Float, nullable=False)

    aquapod = relationship("Aquapod", back_populates="kos_za_smece")


# Sensors


class Pumpa(Base):
    __tablename__ = "pumpa"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    aquapod = relationship("Aquapod", back_populates="pumpa")

    broj_okretaja = Column(Integer, nullable=False)
    total_sati_rada = Column(Integer, nullable=False)
    stanje_alarma = Column(String)

    broj_okretaja_unit_id = Column(Integer, ForeignKey("unit.id"))
    broj_okretaja_unit = relationship(
        "Unit", foreign_keys=[broj_okretaja_unit_id])


class Akumulator(Base):
    __tablename__ = "akumulator"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    aquapod = relationship("Aquapod", back_populates="akumulator")

    struja_punjenja = Column(Float, nullable=False)
    struja_praznjenja = Column(Float, nullable=False)
    napon = Column(Float, nullable=False)
    kapacitet = Column(Float, nullable=False)
    broj_ciklusa = Column(Integer, nullable=False)

    struja_punjenja_unit_id = Column(Integer, ForeignKey("unit.id"))
    struja_praznjenja_unit_id = Column(Integer, ForeignKey("unit.id"))
    napon_unit_id = Column(Integer, ForeignKey("unit.id"))
    kapacitet_unit_id = Column(Integer, ForeignKey("unit.id"))

    struja_punjenja_unit = relationship(
        "Unit", foreign_keys=[struja_punjenja_unit_id])
    struja_praznjenja_unit = relationship(
        "Unit", foreign_keys=[struja_praznjenja_unit_id])
    napon_unit = relationship(
        "Unit", foreign_keys=[napon_unit_id])
    kapacitet_unit = relationship(
        "Unit", foreign_keys=[kapacitet_unit_id])


class SolarniPanel(Base):
    __tablename__ = "solarni_panel"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    aquapod = relationship("Aquapod", back_populates="solarni_panel")

    insolacija = Column(Float, nullable=False)
    napon = Column(Float, nullable=False)
    iskoristivost = Column(Float, nullable=False)
    total_sati_rada = Column(Integer, nullable=False)

    insolacija_unit_id = Column(Integer, ForeignKey("unit.id"))
    napon_unit_id = Column(Integer, ForeignKey("unit.id"))
    iskoristivost_unit_id = Column(Integer, ForeignKey("unit.id"))

    insolacija_unit = relationship(
        "Unit", foreign_keys=[insolacija_unit_id])
    napon_unit = relationship(
        "Unit", foreign_keys=[napon_unit_id])
    iskoristivost_unit = relationship(
        "Unit", foreign_keys=[iskoristivost_unit_id])


class Okolis(Base):
    __tablename__ = "okolis"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    aquapod = relationship("Aquapod", back_populates="okolis")

    dubina_mora = Column(Float, nullable=False)
    temp_mora = Column(Float, nullable=False)
    ph_mora = Column(Float, nullable=False)
    smjer_vjetra = Column(Float, nullable=False)
    snaga_vjetra = Column(Float, nullable=False)
    temp_zraka = Column(Float, nullable=False)

    dubina_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    temp_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    ph_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    smjer_vjetra_unit_id = Column(Integer, ForeignKey("unit.id"))
    snaga_vjetra_unit_id = Column(Integer, ForeignKey("unit.id"))
    temp_zraka_unit_id = Column(Integer, ForeignKey("unit.id"))

    dubina_mora_unit = relationship(
        "Unit", foreign_keys=[dubina_mora_unit_id])
    temp_mora_unit = relationship(
        "Unit", foreign_keys=[temp_mora_unit_id])
    ph_mora_unit = relationship(
        "Unit", foreign_keys=[ph_mora_unit_id])
    smjer_vjetra_unit = relationship(
        "Unit", foreign_keys=[smjer_vjetra_unit_id])
    snaga_vjetra_unit = relationship(
        "Unit", foreign_keys=[snaga_vjetra_unit_id])
    temp_zraka_unit = relationship(
        "Unit", foreign_keys=[temp_zraka_unit_id])

# Audit tables


class PumpaAudit(Base):
    __tablename__ = "pumpa_audit"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    aquapod = relationship("Aquapod", back_populates="pumpa")

    broj_okretaja = Column(Integer, nullable=False)
    total_sati_rada = Column(Integer, nullable=False)
    stanje_alarma = Column(String)

    broj_okretaja_unit_id = Column(Integer, ForeignKey("unit.id"))
    broj_okretaja_unit = relationship(
        "Unit", foreign_keys=[broj_okretaja_unit_id])

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class AkumulatorAudit(Base):
    __tablename__ = "akumulator_audit"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    aquapod = relationship("Aquapod", back_populates="akumulator")

    struja_punjenja = Column(Float, nullable=False)
    struja_praznjenja = Column(Float, nullable=False)
    napon = Column(Float, nullable=False)
    kapacitet = Column(Float, nullable=False)
    broj_ciklusa = Column(Integer, nullable=False)

    struja_punjenja_unit_id = Column(Integer, ForeignKey("unit.id"))
    struja_praznjenja_unit_id = Column(Integer, ForeignKey("unit.id"))
    napon_unit_id = Column(Integer, ForeignKey("unit.id"))
    kapacitet_unit_id = Column(Integer, ForeignKey("unit.id"))

    struja_punjenja_unit = relationship(
        "Unit", foreign_keys=[struja_punjenja_unit_id])
    struja_praznjenja_unit = relationship(
        "Unit", foreign_keys=[struja_praznjenja_unit_id])
    napon_unit = relationship(
        "Unit", foreign_keys=[napon_unit_id])
    kapacitet_unit = relationship(
        "Unit", foreign_keys=[kapacitet_unit_id])

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class SolarniPanelAudit(Base):
    __tablename__ = "solarni_panel_audit"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    aquapod = relationship("Aquapod", back_populates="solarni_panel")

    insolacija = Column(Float, nullable=False)
    napon = Column(Float, nullable=False)
    iskoristivost = Column(Float, nullable=False)
    total_sati_rada = Column(Integer, nullable=False)

    insolacija_unit_id = Column(Integer, ForeignKey("unit.id"))
    napon_unit_id = Column(Integer, ForeignKey("unit.id"))
    iskoristivost_unit_id = Column(Integer, ForeignKey("unit.id"))

    insolacija_unit = relationship(
        "Unit", foreign_keys=[insolacija_unit_id])
    napon_unit = relationship(
        "Unit", foreign_keys=[napon_unit_id])
    iskoristivost_unit = relationship(
        "Unit", foreign_keys=[iskoristivost_unit_id])

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class OkolisAudit(Base):
    __tablename__ = "okolis_audit"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"), unique=True)
    aquapod = relationship("Aquapod", back_populates="okolis")

    dubina_mora = Column(Float, nullable=False)
    temp_mora = Column(Float, nullable=False)
    ph_mora = Column(Float, nullable=False)
    smjer_vjetra = Column(Float, nullable=False)
    snaga_vjetra = Column(Float, nullable=False)
    temp_zraka = Column(Float, nullable=False)

    dubina_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    temp_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    ph_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    smjer_vjetra_unit_id = Column(Integer, ForeignKey("unit.id"))
    snaga_vjetra_unit_id = Column(Integer, ForeignKey("unit.id"))
    temp_zraka_unit_id = Column(Integer, ForeignKey("unit.id"))

    dubina_mora_unit = relationship(
        "Unit", foreign_keys=[dubina_mora_unit_id])
    temp_mora_unit = relationship(
        "Unit", foreign_keys=[temp_mora_unit_id])
    ph_mora_unit = relationship(
        "Unit", foreign_keys=[ph_mora_unit_id])
    smjer_vjetra_unit = relationship(
        "Unit", foreign_keys=[smjer_vjetra_unit_id])
    snaga_vjetra_unit = relationship(
        "Unit", foreign_keys=[snaga_vjetra_unit_id])
    temp_zraka_unit = relationship(
        "Unit", foreign_keys=[temp_zraka_unit_id])

    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))

# Drop all tables
# DROP SCHEMA public CASCADE
# CREATE SCHEMA public
