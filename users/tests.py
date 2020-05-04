from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User



class LoginTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('user1', 'temporary@gmail.com', 'rti3579')

    def test(self):
        client = Client()
        # test false login
        response1 = client.post('/login/', {'username': 'user2', 'password': 'rti3579'})
        self.assertEqual(response1.status_code, 200)


        # login with false password
        response3 = client.post('/login/', {'user1': 'narges', 'password': 'rti357'})
        self.assertEqual(response3.status_code, 200)

        # test true login
        response5 = client.post('/login/', {'username': 'user1', 'password': 'rti3579'})
        self.assertEqual(response5.status_code, 302)


class RegisterTest(TestCase):
    def test(self):
        client = Client()

        #test new user register
        response2 = client.post('/register/', {'username': 'user3','email':'j@gmail.com' , 'password1': 'yuio1234', 'password2': 'yuio1234'})
        self.assertEqual(response2.status_code, 302) # 302 ~ Found

        # check email set or not :
        user = User.objects.get(username='user3')
        self.assertEqual(user.email, 'j@gmail.com')
        # check password set or not :
        self.assertEqual(user.check_password("yuio1234") , True )

        # test register with existed username
        response4 = client.post('/register/', {'username': 'user3', 'email': 'j2@gmail.com', 'password1': 'yuio1234','password2': 'yuio1234'})
        self.assertEqual(response4.status_code, 200)



class ChangePasswordTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('user2', 'j2@gmail.com' , 'yuio1234')


    def test(self):
        client = Client()
        client.login(username='user2', password='yuio1234')

        # change password
        response2 = client.post('/changePassword/', {'old_password': 'yuio1234', 'new_password1': 'yuioo12345' , 'new_password2': 'yuioo12345' })
        self.assertEqual(response2.status_code, 302)

        # test login with old password
        response5 = client.post('/login/', {'username': 'user2', 'password': 'yuio1234'})
        self.assertEqual(response5.status_code, 200)

        # test login with new password
        response5 = client.post('/login/', {'username': 'user2', 'password': 'yuioo12345'})
        self.assertEqual(response5.status_code, 302)

        # check password in database :
        user = User.objects.get(username='user2')
        self.assertEqual(user.check_password("yuioo12345"), True)


class ChangeEmailTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('user4', 'j3@gmail.com' , 'yuio1234')


    def test(self):
        client = Client()
        client.login(username='user4', password='yuio1234')

        # before change email :
        user = User.objects.get(username='user4')
        self.assertEqual(user.email, 'j3@gmail.com')

        # change email :
        response2 = client.post('/changeEmail/', {'email': 'j4@gmail.com' })
        self.assertEqual(response2.status_code, 302)

        # after change email :
        user = User.objects.get(username='user4')
        self.assertEqual(user.email, 'j4@gmail.com')
