from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, ImageField, BooleanField, ForeignKey, CASCADE, IntegerField, Model, \
    DateTimeField, FloatField, PositiveIntegerField, TextField
from django_ckeditor_5.fields import CKEditor5Field


class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    username = CharField(max_length=150, null=True, blank=True, unique=True)
    email = EmailField(unique=True)
    phone = CharField(max_length=25, null=True, blank=True)
    image = ImageField(upload_to='users/%Y/%m', null=True, blank=True)
    is_deleted = BooleanField(default=False)


class Category(CreatedBaseModel):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(CreatedBaseModel):
    owner = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='products/')
    category = ForeignKey('apps.Category', on_delete=CASCADE)

    def __str__(self):
        return self.name


# class ProductImage(CreatedBaseModel):
#     image = ImageField(upload_to='media/images/')
#     product = ForeignKey('apps.Product', CASCADE)
