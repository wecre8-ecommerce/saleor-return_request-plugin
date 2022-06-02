import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from saleor.graphql.core.connection import (
    CountableConnection,
)
from return_request import models


class CountableDjangoObjectType(DjangoObjectType):
    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(cls, *args, **kwargs):
        # Force it to use the countable connection
        countable_conn = CountableConnection.create_type(
            "{}CountableConnection".format(cls.__name__), node=cls
        )
        super().__init_subclass_with_meta__(*args, connection=countable_conn, **kwargs)


class ReturnOrderRequest(CountableDjangoObjectType):
    user = graphene.Field(graphene.ID, description="User ID.")
    order = graphene.Field(graphene.ID, description="Order ID.")

    class Meta:
        interfaces = [relay.Node]
        model = models.ReturnOrderRequest
        description = "Represents a return request."

    def resolve_user(self, info):
        return graphene.Node.to_global_id("User", self.user.id)

    def resolve_order(self, info):
        return graphene.Node.to_global_id("Order", self.order.id)


class ReturnOrderRequestCountableConnection(CountableConnection):
    class Meta:
        updated_field = "status"
        node = ReturnOrderRequest
        name = "ReturnOrderRequestCountableConnection"
        description = "A countable connection to a list of return order requests."
