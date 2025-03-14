from urllib.parse import quote_plus

import requests
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import declarative_base, Session


def custom_api(db, models, data):

    
    languages = data.get('language')
    states = data.get('state')  

    obj = models.UserModel(
        language=languages,
        state=states
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
