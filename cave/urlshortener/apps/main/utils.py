import random
import string
from django.conf import settings

# SHORTCODE_MAX = settings.SHORTCODE_MAX
SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)

# from urlshortener.models import AcadeURL
# ======
# used inside shell from urlshortener.apps.main.models import AcadeURL
# AcadeURL.objects.refresh_shortcodes()
# ======
# chars="abcdefghijklmnopqrstuvwxyz1234"

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    # new_code = ""
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # print("code_generator in models", new_code)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))


#  An instance of the class represents one object from that model (which maps to one row of the table in the database)
def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    # print('instance.__class__ : ', instance.__class__)
    # print('instance.__class__.__name__ :  ', instance.__class__.__name__)
    klass = instance.__class__
    c = klass.objects.all()
    # url = klass.objects.get(url)
    # print('object queryset : ', c)
    # print('object queryset count : ', c.count())
    qs_exists = klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code

