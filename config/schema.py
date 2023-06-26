import graphene
from app.ingredients.schema import Query as IngredientSchema
from app.users.schema import Mutation as UserMutation
from app.users.schema import Query as UserSchema


class SuperQuery(UserSchema, IngredientSchema, graphene.ObjectType):
    pass


class SuperMutation(UserMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=SuperQuery, mutation=SuperMutation)
