#!/usr/bin/python3
# -*- coding:utf-8 -*-


import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.Employee

users_collection = database.get_collection("users_collection")
