from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter
from itertools import repeat, chain
# Create your models here.


@api_view(['POST'])
def lambda_function(request):
    question = request.data
    numbers = question["question"]
    # numbers.sort()

    # aux_dict = {}
    # for i in numbers:
    #     count = 0
    #     for j in numbers:
    #         if (j == i):
    #             count += 1
    #             aux_dict[int(j)] = count
    #     count = 0

    response = list(chain.from_iterable(repeat(x, i)
                                        for x, i in Counter(numbers)
                                        .most_common()))

    return Response({"solution": response})
