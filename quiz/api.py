import graphene
from quiz.queries import (
    QuizQueries, 
    CategoryQueries,
    QuestionQueries,
    AnswerQueries,
)
from quiz.mutations import QuizMutations

#This is the query that brings our data in from the database
#that we then run our customized queries against to search for data
class Query(
    QuizQueries,
    CategoryQueries,
    QuestionQueries,
    AnswerQueries,
    ):
    node = graphene.Node.Field()


# class Mutations(
#     QuizMutations,
#     ):
#     pass

schema = graphene.Schema(query=Query)