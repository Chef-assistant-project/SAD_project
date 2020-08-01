from django import forms

DIET = (
    ("all", "none"),
    ("vegetarian", "vegetarian"),
    ("gluten_free", "gluten free"),
    ("lactose_free", "lactose_free"),
    ("pescatarian", "pescatarian")
)
CUISINE = (
    ("all", "none"),
    ("Asian", "Asian"),
    ("Italian", "Italian"),
    ("Chinese", "Chinese"),
    ("French", "French"),
    ("German", "German"),
    ("mexican", "mexican"),
    ("chinese", "chinese")
)
MEAL_TYPE = (
    ("all", "none"),
    ("breakfast", "breakfast"),
    ("desserts", "desserts"),
    ("dinner", "dinner"),
    ("salads", "salads"),
    ("cakes", "cakes"),
    ("breads", "breads"),
    ("soups", "soups"),
    ("sandwiches", "sandwiches"),
    ("drinks", "drinks"),
    ("seafood", "seafood")
)


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
        self.fields['sauces'].choices = self.SAUCES

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
    SAUCES = ()
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
    sauces = forms.MultipleChoiceField(
        required=False,
        label="sauces",
        choices=SAUCES,
        widget=forms.CheckboxSelectMultiple(),

    )
    legumes = forms.MultipleChoiceField(
        required=False,
        label="legumes",
        choices=LEGUMES,
        widget=forms.CheckboxSelectMultiple(),

    )


class FilterTypesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if FilterTypesForm.ever_filled == False:
            from .models import Food
            FilterTypesForm.SITE = {food.url.split('/')[2].replace("www.", "") for food in Food.objects.all()}
            FilterTypesForm.SITE = (("all","all"),)+tuple((item, item) for item in FilterTypesForm.SITE)
            FilterTypesForm.ever_filled = True
        super(FilterTypesForm, self).__init__(*args, **kwargs)
        self.fields['site'].choices = self.SITE


    SITE = ()
    ever_filled = False
    site = forms.ChoiceField(choices=SITE, label="Site", required=False)
    diet = forms.ChoiceField(choices=DIET, label="Diet", required=False)
    cuisine = forms.ChoiceField(choices=CUISINE, label="Cuisine", required=False)
    mealType = forms.ChoiceField(choices=MEAL_TYPE, label="Meal Type", required=False)

