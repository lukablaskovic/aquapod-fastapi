from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .db import Base


class AquaPod(Base):
    __tablename__ = "aquapod"
    id = Column(Integer, primary_key=True, index=True)
    ime = Column(String, nullable=False)
    gps_position_id = Column(Integer, ForeignKey("gps_position.id"))
    video_cam_id = Column(Integer, ForeignKey("video_cam.id"))
    kos_za_smece_id = Column(Integer, ForeignKey("kos_za_smece.id"))
    pumpa_id = Column(Integer, ForeignKey("pumpa.id"))
    akumulator_id = Column(Integer, ForeignKey("akumulator.id"))
    solarni_panel_id = Column(Integer, ForeignKey("solarni_panel.id"))
    okolis_id = Column(Integer, ForeignKey("okolis.id"))

# General


class VideoCam(Base):
    __tablename__ = "video_cam"
    id = Column(Integer, primary_key=True, index=True)
    is_on = Column(Boolean, nullable=False)
    pan = Column(Float, nullable=False)
    zoom = Column(Float, nullable=False)


class GPSPosition(Base):
    __tablename__ = "gps_position"
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    latitude_unit_id = Column(Integer, ForeignKey("unit.id"))
    longitude = Column(Float, nullable=False)
    longitude_unit_id = Column(Integer, ForeignKey("unit.id"))
    timestamp = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=text("NOW()"))


class KosZaSmece(Base):
    __tablename__ = "kos_za_smece"
    id = Column(Integer, primary_key=True, index=True)
    napunjenost = Column(Float, nullable=False)


class Unit(Base):
    __tablename__ = "unit"
    id = Column(Integer, primary_key=True, index=True)
    naziv = Column(String, nullable=False)
    kratica = Column(String, nullable=False)
    opis = Column(String)


# Sensors
class Pumpa(Base):
    __tablename__ = "pumpa"
    id = Column(Integer, primary_key=True, index=True)
    broj_okretaja = Column(Integer, nullable=False)
    broj_okretaja_unit_id = Column(Integer, ForeignKey("unit.id"))
    total_sati_rada = Column(Integer, nullable=False)
    stanje_alarma = Column(String)


class Akumulator(Base):
    __tablename__ = "akumulator"
    id = Column(Integer, primary_key=True, index=True)
    struja_punjenja = Column(Float, nullable=False)
    struja_punjenja_unit_id = Column(Integer, ForeignKey("unit.id"))
    struja_praznjenja = Column(Float, nullable=False)
    struja_praznjenja_unit_id = Column(Integer, ForeignKey("unit.id"))
    napon = Column(Float, nullable=False)
    napon_unit_id = Column(Integer, ForeignKey("unit.id"))
    kapacitet = Column(Float, nullable=False)
    kapacitet_unit_id = Column(Integer, ForeignKey("unit.id"))
    broj_ciklusa = Column(Integer, nullable=False)


class SolarniPanel(Base):
    __tablename__ = "solarni_panel"
    id = Column(Integer, primary_key=True, index=True)
    insolacija = Column(Float, nullable=False)
    insolacija_unit_id = Column(Integer, ForeignKey("unit.id"))
    napon = Column(Float, nullable=False)
    napon_unit_id = Column(Integer, ForeignKey("unit.id"))
    insolacija = Column(Float, nullable=False)
    insolacija_unit_id = Column(Integer, ForeignKey("unit.id"))
    iskoristivost = Column(Float, nullable=False)
    iskoristivost_unit_id = Column(Integer, ForeignKey("unit.id"))
    total_sati_rada = Column(Integer, nullable=False)


class Okolis(Base):
    __tablename__ = "okolis"
    id = Column(Integer, primary_key=True, index=True)
    dubina_mora = Column(Float, nullable=False)
    dubina_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    temp_mora = Column(Float, nullable=False)
    temp_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    ph_mora = Column(Float, nullable=False)
    ph_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    smjer_vjetra = Column(Float, nullable=False)
    smjer_vjetra_unit_id = Column(Integer, ForeignKey("unit.id"))
    snaga_vjetra = Column(Float, nullable=False)
    snaga_vjetra_unit_id = Column(Integer, ForeignKey("unit.id"))
    temp_zraka = Column(Float, nullable=False)
    temp_zraka_unit_id = Column(Integer, ForeignKey("unit.id"))

# Audit tables


class PumpaAudit(Base):
    __tablename__ = "pumpa_audit"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"))
    broj_okretaja = Column(Integer, nullable=False)
    broj_okretaja_unit_id = Column(Integer, ForeignKey("unit.id"))
    total_sati_rada = Column(Integer, nullable=False)
    stanje_alarma = Column(String)
    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class AkumulatorAudit(Base):
    __tablename__ = "akumulator_audit"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"))
    struja_punjenja = Column(Float, nullable=False)
    struja_punjenja_unit_id = Column(Integer, ForeignKey("unit.id"))
    struja_praznjenja = Column(Float, nullable=False)
    struja_praznjenja_unit_id = Column(Integer, ForeignKey("unit.id"))
    napon = Column(Float, nullable=False)
    napon_unit_id = Column(Integer, ForeignKey("unit.id"))
    kapacitet = Column(Float, nullable=False)
    kapacitet_unit_id = Column(Integer, ForeignKey("unit.id"))
    broj_ciklusa = Column(Integer, nullable=False)
    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class SolarniPanelAudit(Base):
    __tablename__ = "solarni_panel_audit"
    id = Column(Integer, primary_key=True, index=True)
    insolacija = Column(Float, nullable=False)
    insolacija_unit_id = Column(Integer, ForeignKey("unit.id"))
    napon = Column(Float, nullable=False)
    napon_unit_id = Column(Integer, ForeignKey("unit.id"))
    insolacija = Column(Float, nullable=False)
    insolacija_unit_id = Column(Integer, ForeignKey("unit.id"))
    iskoristivost = Column(Float, nullable=False)
    iskoristivost_unit_id = Column(Integer, ForeignKey("unit.id"))
    total_sati_rada = Column(Integer, nullable=False)
    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))


class OkolisAudit(Base):
    __tablename__ = "okolis_audit"
    id = Column(Integer, primary_key=True, index=True)
    aquapod_id = Column(Integer, ForeignKey("aquapod.id"))
    dubina_mora = Column(Float, nullable=False)
    dubina_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    temp_mora = Column(Float, nullable=False)
    temp_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    ph_mora = Column(Float, nullable=False)
    ph_mora_unit_id = Column(Integer, ForeignKey("unit.id"))
    smjer_vjetra = Column(Float, nullable=False)
    smjer_vjetra_unit_id = Column(Integer, ForeignKey("unit.id"))
    snaga_vjetra = Column(Float, nullable=False)
    snaga_vjetra_unit_id = Column(Integer, ForeignKey("unit.id"))
    temp_zraka = Column(Float, nullable=False)
    temp_zraka_unit_id = Column(Integer, ForeignKey("unit.id"))
    operational_timestamp = Column(TIMESTAMP(timezone=True),
                                   nullable=False, server_default=text("NOW()"))
