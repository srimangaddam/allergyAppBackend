from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from restaurantMenus.models import restaurantMenus
from restaurantMenus.serializers import restaurantMenusSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def restaurantMenu_change(request):
    if request.method == 'POST':
        restaurantMenuItem_data = JSONParser().parse(request)
        restaurantMenus_serializer = restaurantMenusSerializer(data=restaurantMenuItem_data)  # noqa: E501
        if restaurantMenus_serializer.is_valid():
            restaurantMenus_serializer.save()
            return JsonResponse(restaurantMenus_serializer.data, status=status.HTTP_201_CREATED)  # noqa: E501
        return JsonResponse(restaurantMenus_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # noqa: E501


@api_view(['GET'])
def restaurantMenu_list(request):
    if request.method == 'GET':
        restaurantMenu = restaurantMenus.objects.all()
        restaurantMenus_serializer = restaurantMenusSerializer(
            restaurantMenu, many=True)
        return JsonResponse(restaurantMenus_serializer.data, safe=False)
