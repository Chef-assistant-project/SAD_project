from django.test import TestCase
from django.test import Client
from blog.models import Food


class CheckDirectSearch(TestCase):

    def setUp(self):
        match = []
        Food.objects.create(
            name='Soft-Boiled Eggs',
            mealType='Breakfast',
            cuisine='all',
            diet='all',
            url='https://www.marthastewart.com/318363/soft-boiled-eggs',
            score=0,
            image='b2.jpg',
            detail='Cooking Perfect Boiled Eggs in minutes'
        )
        Food.objects.create(
            name='fried egg',
            mealType='Breakfast',
            cuisine='all',
            diet='all',
            url='https://cookieandkate.com/favorite-fried-eggs-recipe/',
            score=0,
            image='b2.jpg',
            detail='Cooking Perfect Fried Eggs in minutes'
        )

    def test(self):
        client = Client()
        # test 1 search
        response1 = client.post('/search/', {'title': 'egg'})
        result = (response1.context["matchFoods"] , len(response1.context["matchFoods"]))
        print(result)
        self.assertEqual(str(response1.context["matchFoods"] ) ,  "<QuerySet [<Food: Soft-Boiled Eggs>, <Food: fried egg>]>")
        self.assertEqual(len(response1.context["matchFoods"] ) ,  2)

        # test 2 search
        response1 = client.post('/search/', {'title': 'chicken'})
        result = (response1.context["matchFoods"] , len(response1.context["matchFoods"]))
        print(result)
        self.assertEqual(str(response1.context["matchFoods"] ) ,  "<QuerySet []>")
        self.assertEqual(len(response1.context["matchFoods"] ) ,  0)


