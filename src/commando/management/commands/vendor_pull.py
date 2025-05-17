from django.core.management.base import BaseCommand
from typing import Any
from django.conf import settings
import helper

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
}
STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Download static files")

        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helper.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(name)
            else :
                self.stdout.write(
                    self.style.ERROR(f"failed to download {url}")
                )
        if set(completed_urls) == set(VENDOR_STATICFILES.keys()):
            self.stdout.write(self.style.SUCCESS("successfully uploaded all vendor files"))
        else:
            self.style.WARNING('Something went wrong.')


