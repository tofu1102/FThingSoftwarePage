from django import forms
from .models import Payment
from account_system.models import User


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'description', 'amount', 'payer', 'payee', 'receipt_image']  # receipt_image を追加
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, event, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['payee'].widget = forms.CheckboxSelectMultiple()  # payeeをチェックボックスで選択できるようにする
        self.fields['payee'].queryset = event.members.all()  # payeeの選択肢をイベントのメンバーに制限する
        self.fields['payer'].queryset = event.members.all()