from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from typing import Optional, List
from sqlalchemy.orm import Session
import models
import schemas
from db import get_db

router = APIRouter(
    prefix="/aquapods"
)

# Return all aquapods


@router.get("", response_model=List[schemas.AquaPod])
def getAllAquapods(db: Session = Depends(get_db)):
    try:
        aquapods = db.query(models.AquaPod).all()
    except Exception as e:
        print(e)
    return aquapods

# Return specific aquapod by ID


@router.get("/{name}", response_model=schemas.AquaPod)
def getAquapodByName(name: str, db: Session = Depends(get_db)):
    try:
        aquapod = db.query(models.AquaPod).filter(
            models.AquaPod.name == name).first()
        if not aquapod:
            raise HTTPException(
                status_code=404, detail="Aquapod not found.")
    except Exception as e:
        print(e)
    return aquapod

# Create new Aquapod instance, along with it's components


@router.post("", status_code=status.HTTP_201_CREATED)
def createAquapod(aquapod: schemas.AquaPodCreate, db: Session = Depends(get_db)):
    try:
        new_aquapod = models.AquaPod(**aquapod.dict())
        db.add(new_aquapod)
        db.commit()
        db.refresh(new_aquapod)

        # create components for aquapod

        # VideoCamera(aquapod_id, is_on=false, pan=0.0, zoom=0.0)
        new_video_camera = models.VideoCamera(aquapod_id=new_aquapod.id)
        db.add(new_video_camera)

        # GPSPosition(aquapod_id, latitude=0.0, longitude=0.0)
        new_gps_position = models.GPSPosition(
            aquapod_id=new_aquapod.id)
        db.add(new_gps_position)

        # TrashContainer(aquapod_id, garbage_filled(%) = 0.0)
        new_trash_container = models.TrashContainer(
            aquapod_id=new_aquapod.id)
        db.add(new_trash_container)

        # Pump(aquapod_id, speed(RPM)=0.0, working_time=0.00(min), alarm_status=null)
        new_pump = models.Pump(aquapod_id=new_aquapod.id)
        db.add(new_pump)

        # Battery(aquapod_id, charge_current(A) = 0.0, discharge_current(A)=0.0, voltage(V)=0.0, capacity(Ah)=0.0, cycle_count=0)
        new_battery = models.Battery(aquapod_id=new_aquapod.id)
        db.add(new_battery)

        # Solar_Panel(aquapod_id, insolation(kWh/m2)=0.0, voltage(V)=0.0, utilization(W)=0.0, working_time(min)=0.00)
        new_solar_panel = models.SolarPanel(
            aquapod_id=new_aquapod.id)
        db.add(new_solar_panel)

        # Environment(aquapod_id, sea_depth(m)=0.0, sea_temperature(°C)=0.0, sea_ph(pH)=0.0, wind_direction(°)=0.0, wind_power(km/h)=0.00, air_temperature()=0.00)
        new_environment = models.Environment(aquapod_id=new_aquapod.id)
        db.add(new_environment)

        db.commit()

    except Exception as e:
        print(e)
    return new_aquapod
