from datetime import datetime, timedelta
from typing import Optional
from jose import jwt

from core.configs.settings import settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    delta_expire = (
        expires_delta if expires_delta else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    expire = datetime.utcnow() + delta_expire
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encode_jwt
