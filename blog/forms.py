from django import forms


class ChooseIngredientsForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ChooseIngredientsForm, self).__init__(*args, **kwargs)
        self.fields['dairy'].choices = self.DAIRY
        self.fields['vegetables'].choices = self.VEGETABLES
        self.fields['fruits'].choices = self.FRUITS
        self.fields['backing_and_grains'].choices = self.BACKING_AND_GRAINS
        self.fields['sweeteners'].choices = self.SWEETENERS
        self.fields['spices'].choices = self.SPICES
        self.fields['meats'].choices = self.MEATS
        self.fields['fish_and_seafood'].choices = self.FISH_AND_SEAFOOD
        self.fields['condiments'].choices = self.CONDIMENTS
        self.fields['beverages'].choices = self.BEVERAGES
        self.fields['legumes'].choices = self.LEGUMES
        self.fields['nuts'].choices = self.NUTS
        self.fields['oil'].choices = self.OIL

    DAIRY = ()
    VEGETABLES = ()
    FRUITS = ()
    BACKING_AND_GRAINS = ()
    SWEETENERS = ()
    SPICES = ()
    MEATS = ()
    FISH_AND_SEAFOOD = ()
    CONDIMENTS = ()
    BEVERAGES = ()
    LEGUMES = ()
    NUTS = ()
    OIL = ()

    dairy = forms.MultipleChoiceField(
        required=False,
        label="dairy",
        choices=DAIRY,
        widget=forms.CheckboxSelectMultiple(),
    )
    vegetables = forms.MultipleChoiceField(
        required=False,
        label="vegetables",
        choices=VEGETABLES or "",
        widget=forms.CheckboxSelectMultiple(),

    )
    fruits = forms.MultipleChoiceField(
        required=False,
        label="fruits",
        choices=FRUITS,
        widget=forms.CheckboxSelectMultiple(),

    )
    backing_and_grains = forms.MultipleChoiceField(
        required=False,
        label="backing and rains",
        choices=BACKING_AND_GRAINS,
        widget=forms.CheckboxSelectMultiple(),

    )
    sweeteners = forms.MultipleChoiceField(
        required=False,
        label="sweeteners",
        choices=SWEETENERS,
        widget=forms.CheckboxSelectMultiple(),

    )
    spices = forms.MultipleChoiceField(
        required=False,
        label="spices",
        choices=SPICES,
        widget=forms.CheckboxSelectMultiple(),

    )

    meats = forms.MultipleChoiceField(
        required=False,
        label="meats",
        choices=MEATS,
        widget=forms.CheckboxSelectMultiple(),

    )
    fish_and_seafood = forms.MultipleChoiceField(
        required=False,
        label="fish and seafood",
        choices=FISH_AND_SEAFOOD,
        widget=forms.CheckboxSelectMultiple(),

    )
    condiments = forms.MultipleChoiceField(
        required=False,
        label="condiments",
        choices=CONDIMENTS,
        widget=forms.CheckboxSelectMultiple(),

    )
    beverages = forms.MultipleChoiceField(
        required=False,
        label="beverages",
        choices=BEVERAGES,
        widget=forms.CheckboxSelectMultiple(),

    )
    nuts = forms.MultipleChoiceField(
        required=False,
        label="nuts",
        choices=NUTS,
        widget=forms.CheckboxSelectMultiple(),

    )
    oil = forms.MultipleChoiceField(
        required=False,
        label="oil",
        choices=OIL,
        widget=forms.CheckboxSelectMultiple(),

    )
    legumes = forms.MultipleChoiceField(
        required=False,
        label="legumes",
        choices=LEGUMES,
        widget=forms.CheckboxSelectMultiple(),

    )

