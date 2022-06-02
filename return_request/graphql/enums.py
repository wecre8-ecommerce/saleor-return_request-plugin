from enum import Enum

import graphene


class ReturnOrderRequestErrorCode(Enum):
    INVALID = "invalid"
    REQUIRED = "required"


ReturnOrderRequestErrorCodeType = graphene.Enum.from_enum(ReturnOrderRequestErrorCode)
