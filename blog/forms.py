from django import forms
DIET = (
    ("all", "None"),
    ("vegetarian", "Vegetarian"),
    ("gluten_free", "Gluten free"),
    ("lactose_free", "Lactose_free"),
    ("pescatarian", "Pescatarian")
)
CUISINE = (
    ("all", "None"),
    ("Asian", "Asian"),
    ("Italian", "Italian"),
    ("Chinese", "Chinese"),
    ("French", "French"),
    ("German", "German"),
    ("mexican", "Mexican"),
    ("chinese", "Chinese")
)
MEAL_TYPE = (
    ("all", "None"),
    ("breakfast", "Breakfast"),
    ("desserts", "Desserts"),
    ("dinner", "Dinner"),
    ("salads", "Salads"),
    ("cakes", "Cakes"),
    ("breads", "Breads"),
    ("soups", "Soups"),
    ("sandwiches", "Sandwiches"),
    ("drinks", "Drinks"),
    ("seafood", "Seafood")
)


class ChooseIngredientsForm(forms.Form):
    def __init__(self, *args, **kwargs):

        if ChooseIngredientsForm.ever_filled == False:
            from .models import Ingredient
            ChooseIngredientsForm.DAIRY = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="dairy")))
            ChooseIngredientsForm.BACKING_AND_GRAINS = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="backing_and_grains")))
            ChooseIngredientsForm.SWEETENERS = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="sweeteners")))
            ChooseIngredientsForm.VEGETABLES = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="vegetables")))
            ChooseIngredientsForm.FRUITS = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="fruits")))
            ChooseIngredientsForm.SPICES = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="spices")))
            ChooseIngredientsForm.MEATS = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="meats")))
            ChooseIngredientsForm.FISH_AND_SEAFOOD = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="fish_and_seafood")))
            ChooseIngredientsForm.CONDIMENTS = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="condiments")))
            ChooseIngredientsForm.BEVERAGES = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="beverages")))
            ChooseIngredientsForm.NUTS = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="nuts")))
            ChooseIngredientsForm.OIL = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="oil")))
            ChooseIngredientsForm.LEGUMES = tuple(
                ((item.name, item.name) for item in Ingredient.objects.filter(category="legumes")))
            ChooseIngredientsForm.SAUCES = tuple(
                (item.name, item.name) for item in Ingredient.objects.filter(category="sauces"))
            ChooseIngredientsForm.ever_filled = True

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

    ever_filled = False
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

