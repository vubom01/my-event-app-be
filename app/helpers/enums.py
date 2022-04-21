from enum import Enum


class ApproveEventStatus(Enum):
    APPROVED = 'approved'
    REJECTED = 'rejected'


class StatusEventRequest(Enum):
    INVITED = '0'
    REJECTED = '1'
    APPROVED = '2'
