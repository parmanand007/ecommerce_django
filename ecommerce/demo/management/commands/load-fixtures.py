from typing import Any
from django.core.management import call_command

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args: Any, **kwargs: Any):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata","db_admin_fixture.json"),
        call_command("loaddata","db_category_fixture.json"),
        call_command("loaddata","db_product_fixture.json")
        
        