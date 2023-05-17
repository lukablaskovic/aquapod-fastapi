from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from typing import Optional, List
from sqlalchemy.orm import Session
import models
import schemas
from db import get_db

router = APIRouter(
    prefix="/aquapods"
)


@router.get("", response_model=List[schemas.AquaPod])
def getAllAquapods(db: Session = Depends(get_db)):
    aquapods = []
    try:
        aquapods = db.query(models.AquaPod).all()
    except Exception as e:
        print(e)
    return aquapods


@router.get("/{id}", response_model=schemas.AquaPod)
def getAllAquapods(id: int, db: Session = Depends(get_db)):
    try:
        aquapod = db.query(models.AquaPod).filter(
            models.AquaPod.id == id).first()
    except Exception as e:
        print(e)
    return aquapod


@router.post("", status_code=status.HTTP_201_CREATED)
def createAquapod(aquapod: schemas.AquaPodCreate, db: Session = Depends(get_db)):
    try:
        new_aquapod = models.AquaPod(**aquapod.dict())
        db.add(new_aquapod)
        db.commit()
        db.refresh(new_aquapod)

        # create components for aquapod
        # Pump(aquapod_id, speed(RPM), working_time=0(min), alarm_status=null)
        new_pump = models.Pump(aquapod_id=new_aquapod.id, speed_unit_id=1)
        db.add(new_pump)

        # Battery(aquapod_id, charge_current(A), discharge_current=0(A), voltage=0(V), capacity=0(Ah), cycle_count=0)
        new_battery = models.Battery(aquapod_id=new_aquapod.id, charge_current_unit_id=2,
                                     discharge_current_unit_id=2, voltage_unit_id=3, capacity_unit_id=4)
        db.add(new_battery)

        # Solar_Panel(aquapod_id, insolation(kWh/m2)=0, voltage(V)=0, utilization(W)=0, working_time(min)=0)
        new_solar_panel = models.SolarPanel(
            aquapod_id=new_aquapod.id, insolation_unit_id=6, voltage_unit_id=3, utilization_unit_id=7)
        db.add(new_solar_panel)

        # Environment(aquapod_id, sea_depth, sea_temperature, sea_ph, wind_direction, wind_power, air_temperature)
        new_environment = models.Environment(aquapod_id=new_aquapod.id, sea_depth_unit_id=8, sea_temperature_unit_id=9,
                                             sea_ph_unit_id=10, wind_direction_unit_id=11, wind_power_unit_id=12, air_temperature_unit_id=9)
        db.add(new_environment)
        db.commit()

    except Exception as e:
        print(e)
    return new_aquapod
