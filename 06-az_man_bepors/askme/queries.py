from .models import *
from django.db.models import Avg, Sum, Max, Min


def total_value_of_products():
    return Mobile.objects.aggregate(total_value=Sum('price'))


def total_value_of_products_with_brand_of(brand_name):
    return Mobile.objects.filter(brand__name=brand_name).aggregate(total_value=Sum('price'))


def most_expensive_cheapest_price_with_nationality_of(nationality):
    return Mobile.objects.filter(brand__nationality=nationality).aggregate(cheap=Min('price'), expensive=Max('price'))


def display_size_avg_in_available_mobiles_between_price(minimum, maximum):
    return Mobile.objects.filter(is_available=True, price__gte=minimum, price__lte=maximum).aggregate(avg=Avg('display_size'))
