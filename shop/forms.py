from django import forms

from shop.models import item, usage, store


class itemForm(forms.ModelForm):
    class Meta:
        model=item
        fields=('item_ID','itemName','itemDescription','itemEssentialFlag','itemQty')




class storeForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=item.objects.all(),
                                  to_field_name='itemName',
                                  empty_label="Select Item")

    class Meta:
        model = store
        fields = ('store_ID','store_NAME','item')


class usageForm(forms.ModelForm):
    item= forms.ModelChoiceField(queryset=item.objects.all(),
                                    to_field_name = 'itemName',
                                    empty_label="Select Item")
    class Meta:
        model=usage
        fields=('usage_ID','usagePerc','item')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)