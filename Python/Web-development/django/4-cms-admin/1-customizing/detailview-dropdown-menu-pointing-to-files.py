"""
    DJANGO > CMS > DETAILVIEW: CREATING DROPMENU POITING TO REAL FILES

    If you wanna create a CMS dropmenu where its options are real files in a folder, this solution will help you.

    Basic dropdown menu:
        .../django/9-forms/dropdown-dynamic.py

"""


# STEP 1/3 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Create a apps/my_app/service/what_you_want_scan.py file!

from pathlib import Path
from typing import List

from django.conf import settings as stgs

from .. import consts
from ..models import ModelClassName


class WhatYouWantScanService:
    """This service scans for xxxxxxxxxxxxxxxx to populate dropdown choices in ModelClassName."""

    # TODO: Should implement some caching for this service? I think so!

    @staticmethod
    def get_filenames() -> List[str]:
        """Returns a sorted list of XXXXXXXXXX file names."""
        obj = ModelClassName.objects.first()
        # Escape:
        if (
            # No singleton yet:
            not obj
            # Or no files path configured in obj yet:
            or not obj.path_where_files_are  # This is like "frontend/src/components/pages/"
        ):
            print(f"ERROR SERVICES: WhatYouWantScanService.get_filenames returned empty!")
            return []

        # Building and checking the files base path:
        # (if some wrong, escape!)
        absolute_files_path = Path(stgs.BASE_DIR) / obj.path_where_files_are
        if not absolute_files_path.exists() or not absolute_files_path.is_dir():
            print(f"ERROR SERVICES: WhatYouWantScanService.get_filenames returned empty!")
            return []

        # Finally, successfully it returns files' list:
        files = [file.name for file in absolute_files_path.glob("*.vue") if file.is_file()]
        return sorted(files)


# STEP 2/3 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Form to be used/tied to the model that has the field_to_show_file_names in CMS!

from .services.what_you_want_scan import WhatYouWantScanService

class ModelWhereIsDropmenuForm(forms.ModelForm):
    """Customizing the XXXXXXX detail-view in the CMS. This is important for field_to_show_file_names field!"""

    class Meta:
        model = models.ModelWhereIsDropmenu  # Form tied to this model.
        fields = "__all__"

    # Extra form fields (Not tied to the model):
    # Reserved space...

    def __init__(self, *args, **kwargs):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        super().__init__(*args, **kwargs)
        # Some conditional for the field to be shown:
        obj = models.ModelClassName.objects.first()
        if obj.is_something:
            files = WhatYouWantScanService.get_filenames()
            choices = [("", "--------")] + [(i, i) for i in files]
            # Force the field to render as a dropdown:
            self.fields["field_to_show_file_names"].widget = forms.Select(choices=choices)


# STEP 3/3 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Make sure the Model Admin class is tied to the form.

@admin.register(models.ModelWhereIsDropmenu)
class ModelWhereIsDropmenuAdmin(admin.ModelAdmin):
    # Custom form:
    form = forms.ModelWhereIsDropmenuForm