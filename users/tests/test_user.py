from users.tests import BaseTests
from users.models.mongo import User


class UserTests(BaseTests):
    user_id = 'test id'
    user_pw = 'test pw'

    def test_1_create_user(self):
        user = User(
            user_id=self.user_id,
            user_pw=self.user_pw
        ).save()
        self.assertEqual(type(user), User)

    def test_2_user_exist(self):
        user = User.objects(user_id=self.user_id, user_pw=self.user_pw).first()
        self.assertEqual(type(user), User)

    def test_3_delete_user(self):
        user = User.objects(user_id=self.user_id, user_pw=self.user_pw).delete()
        self.assertEqual(user, 1)
