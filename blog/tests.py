from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.test import Client
from .models import Food
from users.models import Profile
from .views import FoodLiked
from blog import views


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
        print("nnnnn", response1)
        result = (response1.context["matchFoods"], len(response1.context["matchFoods"]))
        print(result)
        self.assertEqual(str(response1.context["matchFoods"]),
                         "<QuerySet [<Food: Soft-Boiled Eggs>, <Food: fried egg>]>")
        self.assertEqual(len(response1.context["matchFoods"]), 2)

        # test 2 search
        response1 = client.post('/search/', {'title': 'chicken'})
        result = (response1.context["matchFoods"], len(response1.context["matchFoods"]))
        print(result)
        self.assertEqual(str(response1.context["matchFoods"]), "<QuerySet []>")
        self.assertEqual(len(response1.context["matchFoods"]), 0)


class CheckFavorites(TestCase):
    F1 = ''
    F2 = ''
    P1 = ''

    def setUp(self):
        global F1, F2, P1
        F1 = Food.objects.create(
            name='Soft-Boiled Eggs',
            mealType='Breakfast',
            cuisine='all',
            diet='all',
            url='https://www.marthastewart.com/318363/soft-boiled-eggs',
            score=0,
            image='b2.jpg',
            detail='Cooking Perfect Boiled Eggs in minutes'
        )
        F2 = Food.objects.create(
            name='fried egg',
            mealType='Breakfast',
            cuisine='all',
            diet='all',
            url='https://cookieandkate.com/favorite-fried-eggs-recipe/',
            score=1,
            image='b2.jpg',
            detail='Cooking Perfect Fried Eggs in minutes'
        )
        self.user = User.objects.create(username='person1')
        P1 = Profile.objects.create(user=self.user)
        self.request_factory = RequestFactory()

    def test(self):
        global F1, F2, P1
        client = Client()
        # test 1 search
        views.FoodChosenForLike = [F1, F2]
        request = self.request_factory.get('/search/',
                                           {'isLike': 'True', 'isProfile': 'False', 'foods': 'Soft-Boiled Eggs',
                                            'action': 'add'})
        request.user = self.user
        response = views.search(request)
        Favorites = P1.favorites.all()
        self.assertEqual(str(Favorites), '<QuerySet [<Food: Soft-Boiled Eggs>]>')
        self.assertEqual(response.status_code, 200)

        # test 2 search
        response2 = client.get('/search/',
                               {'isLike': 'True', 'isProfile': 'False', 'foods': 'fried egg', 'action': 'minus'})
        result2 = response2.json()
        self.assertEqual(result2['likes'], 0)

        # test 3 search
        response3 = client.get('/search/',
                               {'isLike': 'True', 'isProfile': 'False', 'foods': 'Soft-Boiled Eggs', 'action': 'add'})
        result3 = response3.json()
        self.assertEqual(result3['likes'], 2)

        # test 4 search
        request4 = self.request_factory.get('/search/',
                                            {'isLike': 'True', 'isProfile': 'False', 'foods': 'Soft-Boiled Eggs',
                                             'action': 'minus'})
        request4.user = self.user
        response4 = views.search(request4)
        Favorites = P1.favorites.all()
        self.assertEqual(str(Favorites), '<QuerySet []>')
        self.assertEqual(response4.status_code, 200)


