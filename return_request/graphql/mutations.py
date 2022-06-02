import logging

import graphene

from saleor.graphql.core.mutations import ModelMutation
from saleor.graphql.core.types import Error
from return_request.models import ReturnOrderRequest as ReturnOrderRequestModel
from return_request.graphql.enums import ReturnOrderRequestErrorCodeType
from return_request.graphql.types import ReturnOrderRequest

logger = logging.getLogger(__name__)


class OrderRequestInput(graphene.InputObjectType):
    user = graphene.ID(description="User ID.", required=True)
    order = graphene.ID(description="Order ID.", required=True)


class OrderRequestError(Error):
    code = ReturnOrderRequestErrorCodeType(description="The error code.", required=True)


class CreateOrderRequest(ModelMutation):
    return_order_request = graphene.Field(
        ReturnOrderRequest, description="A user instance return order request."
    )

    class Arguments:
        input = OrderRequestInput(
            required=True,
            description="Fields required to create a return order request.",
        )

    class Meta:
        interface = graphene.relay.Node
        model = ReturnOrderRequestModel
        error_type_class = OrderRequestError
        object_type = ReturnOrderRequest
        error_type_field = "return_order_request_errors"
        description = "Create a new ReturnOrderRequest for the customer."

    @classmethod
    def check_permissions(cls, context, permissions=None):
        return context.user.is_authenticated
