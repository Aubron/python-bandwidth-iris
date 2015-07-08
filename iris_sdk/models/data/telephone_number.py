#!/usr/bin/env python

from iris_sdk.models.base_resource import BaseData
from iris_sdk.models.maps.telephone_number import TelephoneNumberMap

class TelephoneNumberData(TelephoneNumberMap, BaseData):

    @property
    def id(self):
        return self.full_number
    @id.setter
    def id(self, id):
        self.full_number = id

    @property
    def last_modified_date(self):
        return self.last_modified
    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        self.last_modified = last_modified_date

    @property
    def telephone_number(self):
        return self.full_number
    @telephone_number.setter
    def telephone_number(self, number):
        self.full_number = number