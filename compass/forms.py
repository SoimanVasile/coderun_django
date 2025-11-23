from django import forms
from .models import Instruction


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['direction', 'distance', 'description',
                  'risk_level', 'previous_instruction']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. Turn right at the skeletal rock...'}),
            'risk_level': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 100, 'step': 1}),
            'direction': forms.Select(attrs={'class': 'direction-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['previous_instruction'].label = "Linked to (Previous Step)"
        self.fields['previous_instruction'].empty_label = "None (Start of a new route)"
        # Optional: Order querysets if needed, e.g., newest first
        self.fields['previous_instruction'].queryset = Instruction.objects.order_by(
            '-id')
