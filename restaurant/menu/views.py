from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Prefetch
from .models import FoodCategory, Food
from .serializers import FoodListSerializer

class FoodCategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = (
            FoodCategory.objects.prefetch_related(
                Prefetch(
                    'food',
                    queryset=Food.objects.filter(is_publish=True),
                    to_attr='published_foods'
                )
            )
            .filter(food__is_publish=True)
            .distinct()
        )

        filtered_categories = [
            category for category in categories if category.published_foods
        ]

        serializer = FoodListSerializer(filtered_categories, many=True)
        return Response(serializer.data)
