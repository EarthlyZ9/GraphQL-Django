import graphene
from graphene_django import DjangoObjectType

from app.users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "email", "name")


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.BigInt(required=True))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user_by_id(root, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        email = graphene.String(required=True)
        name = graphene.String(required=True)

    # The class attributes define the response of the mutation
    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, email, name):
        user = User.objects.create(email=email, name=name)
        user.save()
        # Notice we return an instance of this mutation
        return UserCreateMutation(user=user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    # The class attributes define the response of the mutation
    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id, name):
        try:
            user = User.objects.get(id=id)
            user.name = name
            user.save(update_fields=["name"])
        except User.DoesNotExist:
            return None
        # Notice we return an instance of this mutation
        return UserUpdateMutation(user=user)


class Mutation(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()
