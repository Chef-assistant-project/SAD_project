from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.test import Client
from .models import Food
from users.models import Profile
# from .views import FoodLiked
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
        self.assertEqual(str(response1.context["match_foods"]),
                         "<QuerySet [<Food: Soft-Boiled Eggs>, <Food: fried egg>]>")
        self.assertEqual(len(response1.context["match_foods"]), 2)

        # test 2 search
        response1 = client.post('/search/', {'title': 'chicken'})
        self.assertEqual(str(response1.context["match_foods"]), "<QuerySet []>")
        self.assertEqual(len(response1.context["match_foods"]), 0)


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
        # client = Client()
        # # test 1 search
        # views.FoodChosenForLike = [F1, F2]
        # request = self.request_factory.get('/search/',
        #                                    {'isLike': 'True', 'isProfile': 'False', 'foods': 'Soft-Boiled Eggs',
        #                                     'action': 'add'})
        # request.user = self.user
        # response = views.search(request)
        # Favorites = P1.favorites.all()
        # self.assertEqual(str(Favorites), '<QuerySet [<Food: Soft-Boiled Eggs>]>')
        # self.assertEqual(response.status_code, 200)
        #
        # # test 2 search
        # response2 = client.get('/search/',
        #                        {'isLike': 'True', 'isProfile': 'False', 'foods': 'fried egg', 'action': 'minus'})
        # result2 = response2.json()
        # self.assertEqual(result2['likes'], 0)
        #
        # # test 3 search
        # response3 = client.get('/search/',
        #                        {'isLike': 'True', 'isProfile': 'False', 'foods': 'Soft-Boiled Eggs', 'action': 'add'})
        # result3 = response3.json()
        # self.assertEqual(result3['likes'], 2)
        #
        # # test 4 search
        # request4 = self.request_factory.get('/search/',
        #                                     {'isLike': 'True', 'isProfile': 'False', 'foods': 'Soft-Boiled Eggs',
        #                                      'action': 'minus'})
        # request4.user = self.user
        # response4 = views.search(request4)
        # Favorites = P1.favorites.all()
        # self.assertEqual(str(Favorites), '<QuerySet []>')
        # self.assertEqual(response4.status_code, 200)


class CheckFilterSearch(TestCase):

    def setUp(self):
        food1 = Food.objects.create(
            name='food1',
            mealType='breakfast',
            cuisine='Asian',
            diet='pescatarian',
            url='https://www.marthastewart.com/318363/soft-boiled-eggs',
            score=0,
            image='b2.jpg',
            detail='detail1'
        )
        ingredient1 = food1.ingredients.create(name="ingredient1", category="dairy")
        ingredient1.save()

        food2 = Food.objects.create(
            name='food2',
            mealType='breakfast',
            cuisine='Italian',
            diet='vegetarian',
            url='https://cookieandkate.com/favorite-fried-eggs-recipe/',
            score=0,
            image='b2.jpg',
            detail='detail2'
        )
        food2.ingredients.add(ingredient1)

        food3 = Food.objects.create(
            name='food3',
            mealType='dinner',
            cuisine='Chinese',
            diet='vegetarian',
            url='https://cookieandkate.com/favorite-fried-eggs-recipe/',
            score=0,
            image='b2.jpg',
            detail='detail3'
        )
        food3.ingredients.add(ingredient1)

    def test(self):
        client = Client()
        # test 1 search
        response1 = client.post('/search/',
                                {'dairy': ['ingredient1'], 'diet': ['all'], 'cuisine': ['all'], 'mealType': ['all']})
        self.assertEqual({food.name for food in response1.context["finalSortedFoodChoose"].keys()},
                         {'food1', 'food2', 'food3'})

        # test mealType :
        response1 = client.post('/search/',
                                {'dairy': ['ingredient1'], 'diet': ['all'], 'cuisine': ['all'],
                                 'mealType': ['breakfast']})
        self.assertEqual({food.name for food in response1.context["finalSortedFoodChoose"].keys()},
                         {'food2', 'food1'})
        # test cuisine :
        response1 = client.post('/search/',
                                {'dairy': ['ingredient1'], 'diet': ['all'], 'cuisine': ['Asian'], 'mealType': ['all']})
        self.assertEqual({food.name for food in response1.context["finalSortedFoodChoose"].keys()},
                         {'food1'})

        # test diet :
        response1 = client.post('/search/',
                                {'dairy': ['ingredient1'], 'diet': ['vegetarian'], 'cuisine': ['all'],
                                 'mealType': ['all']})
        self.assertEqual({food.name for food in response1.context["finalSortedFoodChoose"].keys()},
                         {'food3', 'food2'})

        # test diet and cuisine:
        response1 = client.post('/search/',
                                {'dairy': ['ingredient1'], 'diet': ['vegetarian'], 'cuisine': ['Chinese'],
                                 'mealType': ['all']})
        self.assertEqual({food.name for food in response1.context["finalSortedFoodChoose"].keys()},
                         {'food3'})

        # test cuisine and  mealType
        response1 = client.post('/search/',
                                {'dairy': ['ingredient1'], 'diet': ['all'], 'cuisine': ['Asian'],
                                 'mealType': ['breakfast']})
        self.assertEqual({food.name for food in response1.context["finalSortedFoodChoose"].keys()},
                         {'food1'})


class bestFoods(TestCase):
    def setUp(self):
        Food.objects.create(
            name='F1',
            mealType='Breakfast',
            cuisine='all',
            diet='all',
            url='https://www.marthastewart.com/318363/soft-boiled-eggs',
            score=3,
            image='b2.jpg',
            detail=' '
        )
        Food.objects.create(
            name='F2',
            mealType='Breakfast',
            cuisine='all',
            diet='all',
            url='https://cookieandkate.com/favorite-fried-eggs-recipe/',
            score=1,
            image='b2.jpg',
            detail=' '
        )
        Food.objects.create(
            name='F3',
            mealType='desserts',
            cuisine='all',
            diet='all',
            url='https://www.marthastewart.com/318363/soft-boiled-eggs',
            score=2,
            image='b2.jpg',
            detail=' '
        )
        Food.objects.create(
            name='F4',
            mealType='Breakfast',
            cuisine='all',
            diet='all',
            url='https://www.marthastewart.com/318363/soft-boiled-eggs',
            score=0,
            image='b2.jpg',
            detail=' '
        )

    def test(self):
        client = Client()
        response1 = client.post('//')
        self.assertEqual(len(response1.context["best_food_score"]), 3)
        self.assertEqual(list(response1.context['best_food_score'])[0].name, 'F1')
        self.assertEqual(list(response1.context['best_food_score'])[1].name, 'F3')
        self.assertEqual(list(response1.context['best_food_score'])[2].name, 'F2')


#
# class checkScoreFood(TestCase):
#     def setUp(self):
#         Food.objects.create(
#             name='F1',
#             mealType='Breakfast',
#             cuisine='all',
#             diet='all',
#             url='https://www.marthastewart.com/318363/soft-boiled-eggs',
#             score=3,
#             number_of_score=2,
#             image='b2.jpg',
#             detail=' '
#         )
#         Food.objects.create(
#             name='F2',
#             mealType='Breakfast',
#             cuisine='all',
#             diet='all',
#             url='https://cookieandkate.com/favorite-fried-eggs-recipe/',
#             score=0,
#             number_of_score=1,
#             image='b2.jpg',
#             detail=' '
#         )
#
#
#     def test(self):
#         client = Client()
#         response1 = client.get('/like/', {'name': 'F1', 'index_selected': 3})
        # print(">>>>>>>>>>>>>>>>>>.", response1.)
        # self.assertEqual(response1.json()['like'], 0)

#
# class MySeleniumTests(StaticLiveServerTestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.driver = webdriver.Chrome('D:/program-download/chromedriver')
#         cls.selenium.implicitly_wait(10)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.close()
#         super().tearDownClass()
#
#     def test_login(self):
#         driver = self.driver
#         driver.get("http://127.0.0.1:8000/")
#         assert 'Dish' in driver.page_source
