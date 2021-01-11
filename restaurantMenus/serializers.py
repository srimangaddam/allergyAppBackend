from rest_framework import serializers
from restaurantMenus.models import restaurantMenus


class restaurantMenusSerializer(serializers.ModelSerializer):

    class Meta:
        model = restaurantMenus
        fields = ('id',
                  'brand',
                  'menuItem',
                  'ingredients')
