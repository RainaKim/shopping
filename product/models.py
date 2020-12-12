from django.db import models
from user.models import User

class Product(models.Model):
    name            = models.CharField(max_length = 50)
    price           = models.DecimalField(max_digits = 10, decimal_places = 2)
    created_at      = models.DateTimeField(auto_now_add = True)
    owner           = models.ForeignKey(User,on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'products'
