from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from typing import Optional, List
from sqlalchemy.orm import Session
import models
import schemas
import utils

from db import get_db

router = APIRouter(
    prefix="/aquapods",
    tags=["AquaPod"]
)

# Return all aquapods


@router.get("/", response_model=List[schemas.Aquapod], status_code=status.HTTP_200_OK)
def get_all_aquapods(db: Session = Depends(get_db)):
    try:
        aquapods = db.query(models.AquaPod).all()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An error occurred. {e}")
    return aquapods

# Return specific aquapod by Name


@router.get("/{name}", response_model=Optional[schemas.AquaPodWithLatestData], status_code=status.HTTP_200_OK)
def get_aquapod_by_name(name: str, db: Session = Depends(get_db)):
    try:
        aquapod = db.query(models.AquaPod).filter(
            models.AquaPod.name == name).first()

        if not aquapod:
            raise HTTPException(
                status_code=404, detail="Aquapod not found.")
        print(aquapod)
        latest_data = [
            {"component": "video_camera", "data":
             db.query(models.VideoCamera).filter(
                 models.VideoCamera.aquapod_id == aquapod.id).order_by(
                 models.VideoCamera.id.desc()).first()},
            {"component": "gps_position", "data":
             db.query(models.GPSPosition).filter(
                 models.GPSPosition.aquapod_id == aquapod.id).order_by(
                 models.GPSPosition.id.desc()).first()},
            {"component": "trash_container", "data":
             db.query(models.TrashContainer).filter(
                 models.TrashContainer.aquapod_id == aquapod.id).order_by(
                 models.TrashContainer.id.desc()).first()},
            {"component": "pump", "data":
             db.query(models.Pump).filter(
                 models.Pump.aquapod_id == aquapod.id).order_by(
                 models.Pump.id.desc()).first()},
            {"component": "battery", "data":
             db.query(models.Battery).filter(
                 models.Battery.aquapod_id == aquapod.id).order_by(
                 models.Battery.id.desc()).first()},
            {"component": "solar_panel", "data":
             db.query(models.SolarPanel).filter(
                 models.SolarPanel.aquapod_id == aquapod.id).order_by(
                 models.SolarPanel.id.desc()).first()},
            {"component": "environment", "data":
             db.query(models.Environment).filter(
                 models.Environment.aquapod_id == aquapod.id).order_by(
                 models.Environment.id.desc()).first()}
        ]

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An error occurred. {e}")
    aquapod.latest_data = latest_data
    return aquapod


# Create new Aquapod instance, along with it's components


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_aquapod(aquapod: schemas.AquaPodCreate, db: Session = Depends(get_db)):
    try:
        new_aquapod = models.AquaPod(**aquapod.dict())
        db.add(new_aquapod)
        db.flush()

        # create components for aquapod

        # VideoCamera(aquapod_id, is_on=false, pan=0.0, zoom=0.0)
        video_camera_data = schemas.VideoCameraCreate(
            aquapod_id=new_aquapod.id)
        new_video_camera = models.VideoCamera(**video_camera_data.dict())
        db.add(new_video_camera)

        # GPSPosition(aquapod_id, latitude=0.0, longitude=0.0)
        gps_position_data = schemas.GPSPositionCreate(
            aquapod_id=new_aquapod.id)
        new_gps_position = models.GPSPosition(**gps_position_data.dict())
        db.add(new_gps_position)

        # TrashContainer(aquapod_id, garbage_filled(%) = 0.0)
        trash_container_data = schemas.TrashContainerCreate(
            aquapod_id=new_aquapod.id)
        new_trash_container = models.TrashContainer(
            **trash_container_data.dict())
        db.add(new_trash_container)

        # Pump(aquapod_id, speed(RPM)=0.0, working_time=0.00(min), alarm_status=null)
        pump_data = schemas.PumpCreate(aquapod_id=new_aquapod.id)
        new_pump = models.Pump(**pump_data.dict())
        db.add(new_pump)

        # Battery(aquapod_id, charge_current(A) = 0.0, discharge_current(A)=0.0, voltage(V)=0.0, capacity(Ah)=0.0, cycle_count=0)
        battery_data = schemas.BatteryCreate(aquapod_id=new_aquapod.id)
        new_battery = models.Battery(**battery_data.dict())
        db.add(new_battery)

        # Solar_Panel(aquapod_id, insolation(kWh/m2)=0.0, voltage(V)=0.0, utilization(W)=0.0, working_time(min)=0.00)
        solar_panel_data = schemas.SolarPanelCreate(aquapod_id=new_aquapod.id)
        new_solar_panel = models.SolarPanel(
            **solar_panel_data.dict())
        db.add(new_solar_panel)

        # Environment(aquapod_id, sea_depth(m)=0.0, sea_temperature(°C)=0.0, sea_ph(pH)=0.0, wind_direction(°)=0.0, wind_power(km/h)=0.00, air_temperature()=0.00)
        environment_data = schemas.EnvironmentCreate(aquapod_id=new_aquapod.id)
        new_environment = models.Environment(**environment_data.dict())
        db.add(new_environment)

        db.commit()
        db.refresh(new_aquapod)

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An error occurred. {e}")
    return new_aquapod

# Get aquapod VIDEO CAMERA


@router.get("/{name}/video-camera", response_model=schemas.VideoCamera, status_code=status.HTTP_200_OK)
def get_video_camera_of_aquapod(name: str, db: Session = Depends(get_db)):
    aquapod = db.query(models.AquaPod).filter(
        models.AquaPod.name == name).first()
    if aquapod is None:
        raise HTTPException(
            status_code=404, detail=f"Aquapod '${name}' not found")
    video_camera = db.query(models.VideoCamera).filter(
        models.VideoCamera.aquapod_id == aquapod.id).first()
    if video_camera is None:
        raise HTTPException(
            status_code=404, detail=f"Video camera of Aquapod '${name}' not found!")
    return video_camera

# Get aquapod GPS POSITION


@router.get("/{name}/gps-position", response_model=schemas.GPSPosition, status_code=status.HTTP_200_OK)
def get_gps_position_of_aquapod(name: str, db: Session = Depends(get_db)):
    aquapod = db.query(models.AquaPod).filter(
        models.AquaPod.name == name).first()
    if aquapod is None:
        raise HTTPException(
            status_code=404, detail=f"Aquapod '${name}' not found")
    gps_position = db.query(models.GPSPosition).filter(
        models.GPSPosition.aquapod_id == aquapod.id).first()
    if gps_position is None:
        raise HTTPException(
            status_code=404, detail=f"GPS Position of Aquapod '${name}' not found!")
    return gps_position

# Get aquapod TRASH CONTAINER


@router.get("/{name}/trash-container", response_model=schemas.TrashContainer, status_code=status.HTTP_200_OK)
def get_trash_container_of_aquapod(name: str, db: Session = Depends(get_db)):
    aquapod = db.query(models.AquaPod).filter(
        models.AquaPod.name == name).first()
    if aquapod is None:
        raise HTTPException(
            status_code=404, detail=f"Aquapod '${name}' not found")
    trash_container = db.query(models.TrashContainer).filter(
        models.TrashContainer.aquapod_id == aquapod.id).first()
    if trash_container is None:
        raise HTTPException(
            status_code=404, detail=f"Trash container of Aquapod '${name}' not found!")
    return trash_container

# Get aquapod PUMP


@router.get("/{name}/pump", response_model=schemas.Pump, status_code=status.HTTP_200_OK)
def get_pump_of_aquapod(name: str, db: Session = Depends(get_db)):
    aquapod = db.query(models.AquaPod).filter(
        models.AquaPod.name == name).first()
    if aquapod is None:
        raise HTTPException(
            status_code=404, detail=f"Aquapod '${name}' not found")
    pump = db.query(models.Pump).filter(
        models.Pump.aquapod_id == aquapod.id).first()
    if pump is None:
        raise HTTPException(
            status_code=404, detail=f"Pump of Aquapod '${name}' not found!")
    return pump

# Get aquapod BATTERY


@router.get("/{name}/battery", response_model=schemas.Battery, status_code=status.HTTP_200_OK)
def get_battery_of_aquapod(name: str, db: Session = Depends(get_db)):
    aquapod = db.query(models.AquaPod).filter(
        models.AquaPod.name == name).first()
    if aquapod is None:
        raise HTTPException(
            status_code=404, detail=f"Aquapod '${name}' not found")
    battery = db.query(models.Battery).filter(
        models.Battery.aquapod_id == aquapod.id).first()
    if battery is None:
        raise HTTPException(
            status_code=404, detail=f"Battery of Aquapod '${name}' not found!")
    return battery

# Get aquapod SOLAR PANEL


@router.get("/{name}/solar-panel", response_model=schemas.SolarPanel, status_code=status.HTTP_200_OK)
def get_solar_panel_of_aquapod(name: str, db: Session = Depends(get_db)):
    aquapod = db.query(models.AquaPod).filter(
        models.AquaPod.name == name).first()
    if aquapod is None:
        raise HTTPException(
            status_code=404, detail=f"Aquapod '${name}' not found")
    solar_panel = db.query(models.SolarPanel).filter(
        models.SolarPanel.aquapod_id == aquapod.id).first()
    if solar_panel is None:
        raise HTTPException(
            status_code=404, detail=f"Solar panel of Aquapod '${name}' not found!")
    return solar_panel

# Get aquapod ENVIRONMENT


@router.get("/{name}/environment", response_model=schemas.Environment, status_code=status.HTTP_200_OK)
def get_environment_of_aquapod(name: str, db: Session = Depends(get_db)):
    aquapod = db.query(models.AquaPod).filter(
        models.AquaPod.name == name).first()
    if aquapod is None:
        raise HTTPException(
            status_code=404, detail=f"Aquapod '${name}' not found")
    environment = db.query(models.Environment).filter(
        models.Environment.aquapod_id == aquapod.id).first()
    if environment is None:
        raise HTTPException(
            status_code=404, detail=f"Environment of Aquapod '${name}' not found!")
    return environment
