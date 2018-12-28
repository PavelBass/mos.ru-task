from enum import Enum


class ServiceResultStatus(Enum):
    Ok = 'Found relevant data'
    NoResult = 'No result for passed query'
