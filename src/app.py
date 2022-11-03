from flask import Flask
from flask_graphql import GraphQLView

from context import get_context
from schema import schema

app = Flask(__name__)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True,
        get_context=get_context,
    ),
)

if __name__ == "__main__":
    app.run()
