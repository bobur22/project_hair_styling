from django.contrib import admin
from .models import PostModel,SecPI1_Model, MastersModel, PriceModel, ReportsModel, Categories, BookingModel

admin.site.register(PostModel)
admin.site.register(SecPI1_Model)
admin.site.register(MastersModel)
admin.site.register(PriceModel)
admin.site.register(ReportsModel)
admin.site.register(Categories)
admin.site.register(BookingModel)