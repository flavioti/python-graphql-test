import os

from flask import Flask, redirect
from flask_graphql import GraphQLView

from database import db_session
from schema import schema

app = Flask(__name__)
app.debug = True
app.testing = True

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True, context={"session": db_session}
    ),
)


@app.route("/")
def graphql_redirect():
    return redirect("/graphql", code=302)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
