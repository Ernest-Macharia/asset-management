from django import forms

from asset.models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        exclude = []
