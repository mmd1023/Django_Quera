from .models import Brand, Mobile


def list_all_brands():
    return Brand.objects.all()


def list_all_mobiles():
    return Mobile.objects.all()


def price_of_mobile_with_model(model):
    return Mobile.objects.get(model=model).price


def most_expensive_mobile():
    return Mobile.objects.order_by('-price').first()


def all_mobiles_with_brand_of(brand_name):
    return Mobile.objects.filter(brand__name = brand_name)


def all_available_mobiles_with_price_in_range(min_price, max_price):
    return Mobile.objects.filter(is_available=True, price__gte=min_price, price__lte=max_price).count()

