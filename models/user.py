#!/usr/bin/python3
# -*- coding:utf-8 -*-

from pydantic import BaseModel, Field
from uuid import uuid4


class User(BaseModel):
    user_id: uuid4 = uuid4()
    user_name: str = Field(description="minimum 3 character", min_length=3)
    password: str = Field(description="password must be min 8 character.", min_length=8)
    name:  str = Field(description="minimum 3 character", min_length=3)
    age: int = Field(gt=17, description="age must be above 18.")
    designation: str = Field(description="mention the designation.")
    location: str = Field("mention your location", min_length=3)
