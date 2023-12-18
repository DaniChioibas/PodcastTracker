from django.core.management.base import BaseCommand
from podcasts.utils import spotifyepisodes

class Command(BaseCommand):
    help = 'Command for importing latest spotify episodes of shows currently stored.'

    def handle(self, *args, **options):
        # Your logic for the management command
        spotifyepisodes()
        self.stdout.write(self.style.SUCCESS('Episodes imported!'))