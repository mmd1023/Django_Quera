from .models import Brand, Mobile
from django.db.models import F, Q


def all_brands_not_in_korea_china():
    return Brand.objects.filter(~Q(nationality='China') & ~Q(nationality='Korea'))


def some_brand_mobiles(*brand_names):
    return Mobile.objects.all() if len(brand_names) == 0 else Mobile.objects.filter(brand__name__in=brand_names)


def mobiles_brand_nation_equals_made_in():
    return Mobile.objects.filter(brand__nationality=F('made_in'))
