from django.conf import settings
from django.db import models
from django_hosts.resolvers import reverse
# from django.urls import reverse
from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

# SHORTCODE_MAX = settings.SHORTCODE_MAX
SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class AcadeURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(AcadeURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs
    # function made to change all the shortcodes at the same time.
    def refresh_shortcodes(self):
        qs = AcadeURL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            print("qq", q)
            q.shortcode = create_shortcode(q)
            print('q.shortcode :', q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made:  {i}".format(i=new_codes)


class AcadeURL(models.Model):
    url = models.CharField(max_length=300, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = AcadeURLManager()

    # The keyword arguments are the names of the fields you’ve defined on your model.
    # The save method is an inherited method from models.Model which is executed to save an instance into a particular Model. Whenever one tries to create an instance of a model either from admin interface or django shell, save() function is run.
    # We can override save function before storing the data in the database to apply some constraint or fill some ready only fields like SlugField.
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
            if not "http" in self.url:
                self.url = 'http://' + self.url
        super(AcadeURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("main:scode", kwargs={"shortcode": self.shortcode}, host='www', scheme='http')
        return url_path



