# yourapp/management/commands/your_command.py
from django.core.management.base import BaseCommand
from podcasts.utils import spotify

class Command(BaseCommand):
    help = 'Command for importing spotify shows from their API based on a search querry hard coded.'

    def handle(self, *args, **options):
        # Your logic for the management command
        spotify()
        self.stdout.write(self.style.SUCCESS('Shows imported!'))
