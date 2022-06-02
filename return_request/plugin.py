from saleor.graphql.views import GraphQLView
from saleor.plugins.base_plugin import BasePlugin
from return_request.graphql.schema import schema


class ReturnRequestPlugin(BasePlugin):
    name = "return_request"
    PLUGIN_ID = "return_request"
    PLUGIN_NAME = "Return Request"
    DEFAULT_ACTIVE = True
    CONFIGURATION_PER_CHANNEL = False
    PLUGIN_DESCRIPTION = "Plugin responsible for managing the order return requests."

    def webhook(self, request, path, previous_value):
        request.app = self
        view = GraphQLView.as_view(schema=schema)
        return view(request)
