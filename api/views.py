from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter
from itertools import repeat, chain
# Create your models here.


@api_view(['POST'])
def lambda_function(request):
    question = request.data
    numbers = question["question"]

    response = list(chain.from_iterable(repeat(x, i)
                                        for x, i in Counter(numbers)
                                        .most_common()))

    return Response({"solution": response})
