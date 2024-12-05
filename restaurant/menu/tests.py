from django.test import TestCase
from .models import FoodCategory, Food

class FoodCategoryAPITest(TestCase):
    def setUp(self):
        self.category = FoodCategory.objects.create(name_ru="Напитки", order_id=10)
        Food.objects.create(category=self.category, name_ru="Чай", is_publish=True, cost="123.00", code=1, internal_code=100)

    def test_api_response(self):
        response = self.client.get('/api/v1/foods/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Напитки', response.json()[0]['name_ru'])
