from django.core.management.base import BaseCommand, CommandError
from ....main.models import AcadeURL

class Command(BaseCommand):
    help = "Refreshes all AcadeURL shortcodes"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        return AcadeURL.objects.refresh_shortcodes()