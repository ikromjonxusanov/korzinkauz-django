from django.db.models import *
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.fields import BLANK_CHOICE_DASH
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
class CustomUserManagerModel(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("user_type", 5)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class UserModel(AbstractUser):
    """
    User accounts model.
    """

    username = None
    email = EmailField(
        unique=True, error_messages={'unique': 'Email already in use.'})
    image = ImageField(upload_to='profile-images/', default='default-user.png')
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    passport_code = CharField(max_length=9, validators=[MinLengthValidator(9), MaxLengthValidator(9)], null=True, blank=True)
    user_type = IntegerField(choices=(
        (1, 'vendor'),
        (2, 'accountant'),
        (3, 'productmanager'),
        (4, 'director'),
        (5, 'admin')
    ), default=1)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManagerModel()


    def __str__(self):
        return self.email
    class Meta:
        verbose_name = "User"

class Category(Model):
    name = CharField(max_length=80)
    description = TextField()
    def __str__(self) -> str:
        return self.name

class Product(Model):
    name = CharField(max_length=100)
    code = CharField(max_length=10)
    price = FloatField(validators=[MinValueValidator(0.0)])
    quantities = IntegerField(default=0, validators=[MinValueValidator(0)])
    create_date = DateTimeField(auto_now_add=True)
    duedate = DateField(blank=True)
    category = ForeignKey(Category, null=True, on_delete=SET_NULL)
    def __str__(self) -> str:
        return self.name
class ProductItems(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    quantities = IntegerField(validators=[MinValueValidator(0)])
    sub_price = FloatField(validators=[MinValueValidator(0.0)])
    create_date = DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.product.name

class Order(Model):
    code = CharField(max_length=20)
    products = ManyToManyField(ProductItems)
    sub_price = FloatField(validators=[MinValueValidator(0.0)])
    status = BooleanField(default=False)
    orderTime = TimeField(auto_now_add=True)
    date = DateField(auto_now_add=True)
    create_date = DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.code