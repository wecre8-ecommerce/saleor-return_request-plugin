import graphene
from graphene_federation import build_schema

from saleor.graphql.core.connection import create_connection_slice
from saleor.graphql.core.fields import ConnectionField
from return_request.models import ReturnOrderRequest as ReturnOrderRequestModel
from return_request.graphql.mutations import CreateOrderRequest
from return_request.graphql.types import ReturnOrderRequest, ReturnOrderRequestCountableConnection


class Query(graphene.ObjectType):
    return_order_requests = ConnectionField(
        ReturnOrderRequestCountableConnection,
        description="List of the return order request.",
    )

    @staticmethod
    def resolve_return_order_requests(root, info, **kwargs):
        qs = ReturnOrderRequestModel.objects.all()
        return create_connection_slice(
            qs, info, kwargs, ReturnOrderRequestCountableConnection
        )


class Mutation(graphene.ObjectType):
    order_request_create = CreateOrderRequest.Field()


schema = build_schema(query=Query, mutation=Mutation, types=[ReturnOrderRequest])
