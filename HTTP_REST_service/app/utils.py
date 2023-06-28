from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Units


unit_map = {
    "revolutions_per_minute": 1,
    "ampere": 2,
    "volt": 3,
    "ampere-hour": 4,
    "watt-hour": 5,
    "insolation": 6,
    "watt": 7,
    "meter": 8,
    "degree_celsius": 9,
    "pH": 10,
    "degree": 11,
    "kilometer_per_hour": 12,
    "knot": 13,
    "gram": 14
}
