from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class PostModel(models.Model):
    img = models.ImageField(upload_to="post/")
    text = models.CharField(max_length=30)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name='Post'
        verbose_name_plural="Posts"

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SecPI1_Model(models.Model):
    # Categories = (
    #     ("Manicure", "Маникюр"),
    #     ("Makeup", "Макияж"),
    #     ("Hairdresser", "Парикмахерский")
    # )

    img = models.ImageField(upload_to="secPI1/")
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

    # categories = models.CharField(max_length=30, null=True, choices=Categories)
    # admin_id = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.categories}"

    class Meta:
        verbose_name='Picture'
        verbose_name_plural="Pictures"


class MastersModel(models.Model):
    img = models.ImageField(upload_to="master/")
    text_n = models.CharField(max_length=100)
    text_w = models.CharField(max_length=100, null=True, blank=True, default="lorem10")
    text = models.TextField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.text_n

    class Meta:
        verbose_name='Master'
        verbose_name_plural="Masters"


class PriceModel(models.Model):
    Side = (
        ("r", "Right"),
        ("l", "Left")
    )
    img = models.ImageField(upload_to="price/", default="price/mas_1_3.jpg")
    h1 = models.CharField(max_length=30, null=True, blank=True)
    price1 = models.PositiveIntegerField(null=True, blank=True)
    text1 = models.TextField(null=True, blank=True)
    h2 = models.CharField(max_length=30, null=True, blank=True)
    price2 = models.PositiveIntegerField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    h3 = models.CharField(max_length=30, null=True, blank=True)
    price3 = models.PositiveIntegerField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    h4 = models.CharField(max_length=30, null=True, blank=True)
    price4 = models.PositiveIntegerField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    is_side = models.CharField(choices=Side, max_length=10, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Price and other info"

    class Meta:
        verbose_name='Price'
        verbose_name_plural="Prices"

class ReportsModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_num = models.CharField(max_length=13)
    text = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name="Report"
        verbose_name_plural="Reports"

class BookingModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_num = models.CharField(max_length=13)
    date = models.DateField()
    time = models.TimeField()
    master = models.ForeignKey(MastersModel, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name="Booking"
        verbose_name_plural="Bookings"