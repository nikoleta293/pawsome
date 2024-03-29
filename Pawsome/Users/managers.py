from email.headerregistry import UniqueSingleAddressHeader
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email,username,password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        if not username:
            raise ValueError(('The Username must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email,username=username,password=password ,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user