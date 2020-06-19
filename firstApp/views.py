from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your models here.


@api_view(['POST'])
def handle_post_question(request):
    question = request.data
    numbers = question["question"]
    numbers.sort()

    aux_dict = {}
    for i in numbers:
        count = 0
        for j in numbers:
            if (j == i):
                count += 1
                aux_dict[int(j)] = count
        count = 0

    return Response(aux_dict)
