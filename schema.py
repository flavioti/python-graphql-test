import graphene
from graphene import ObjectType, String
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import PersonModel, UserModel


class PersonSchema(SQLAlchemyObjectType):
    class Meta:
        model = PersonModel
        description = "Teste descrição"
        interfaces = (graphene.relay.Node,)
        fields = "__all__"


class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        fields = "__all__"
        interfaces = (graphene.relay.Node,)


class Query(ObjectType):
    node = graphene.relay.Node.Field()

    person = graphene.Field(PersonSchema)
    people = graphene.List(PersonSchema)

    user = graphene.Field(UserSchema, iduser=graphene.Int())
    users = graphene.List(UserSchema,)  # limit=graphene.Int()

    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    def resolve_person(self, info):
        query = PersonSchema.get_query(info)
        return query.get()

    def resolve_people(self, info):
        query = PersonSchema.get_query(info)
        return query.all()

    def resolve_user(self, info, **args):
        print(info)
        query = UserSchema.get_query(info)
        iduser = args.get("iduser")
        return query.get(iduser)

    def resolve_users(self, info, **kwargs):
        query = UserSchema.get_query(info)
        # limit = args.get("limit")
        return query.query_with_argument()

    # def user_by_name(self, info, **args)
    #     query.

    def resolve_hello(root, info, name):
        return f"Hello {name}!"

    def resolve_goodbye(root, info):
        query_with_argument = '{ hello(name: "GraphQL") }'
        result = schema.execute(query_with_argument)
        print(result.data["hello"])
        return "See ya!"


schema = graphene.Schema(query=Query)
