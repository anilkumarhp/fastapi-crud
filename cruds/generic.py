#!/usr/bin/python3
# -*- coding:utf-8 -*-

from abc import ABC, abstractmethod
from utility.exceptions import EmployeeException, EmployeeDataNotFound


class Crud(ABC):

    def __init__(self):
        self.data = None

    @abstractmethod
    async def create(self, collection, data):
        result = await collection.insert_one(dict(data))
        if result.inserted_id:
            return True
        raise EmployeeException(str(result))

    @abstractmethod
    async def get(self, collection, user_id, **kwargs):
        response = await collection.find_one({"user_id": user_id})
        return response

    @abstractmethod
    async def update(self, collection, **data):
        data = dict(data)
        if len(data):
            raise EmployeeDataNotFound(f"cannot update to {collection}, data is empty.")

        response = await collection.find_one({"user_id": data["user_id"]})

        if response:
            updated_student = await collection.update_one(
                {"user_id": data["user_id"]}, {"$set": data}
            )
            if updated_student:
                return True
            return False

    @abstractmethod
    async def delete(self, collection, user_id):
        user = await collection.find_one({"user_id": user_id})

        if user:
            response = await collection.delete_one({"user_id": user_id})
            if response:
                return True
