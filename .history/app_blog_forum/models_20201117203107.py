from django.db import models
import re

class UserManager(models.Manager):
    def user_registration_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(post_data['first_name']) < 3:
            errors['first_name'] = "First name must be 3 characters"

        if post_data['first_name'].isalpha() == False:
            errors['first_name'] = "letters only"

        if len(post_data['last_name']) < 3:
            errors['last_name'] = "Last name must be 3 characters"

        if post_data['last_name'].isalpha() == False:
            errors['last_name'] = "letters only"

        if len(post_data['email']) < 8:
            errors['email'] = "Email must contain 8 characters"

        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"

        if post_data['password'] != post_data['confirm_password']:
            errors['pass_match'] = "password must match confirm password"

        if len(post_data['password']) < 8:
            errors['pass_length'] = "password must be longer than 8 characters"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30 unique=True)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
