import graphene
from books.queries import BookQueries
from books.mutations import BookMutations
#import all the Queries and Mutations

#This is the query that brings our data in from the database
#that we then run our customized queries against to search for data
class Query(
    BookQueries,
    ):
    node = graphene.Node.Field()


# class Mutations(
#     BookMutations,
#     ):
#     pass

schema = graphene.Schema(query=Query)