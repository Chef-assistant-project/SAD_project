from django import forms

DAIRY = (
    ("butter", "butter"),
    ("egg", "egg"),
    ("milk", "milk")
)
VEGETABLES = (
    ("onion", "onion"),
    ("garlic", "garlic"),
    ("tomato", "tomato"),
    ("potato", "potato"),
    ("carrot", "carrot"),
    ("bell pepper", "bell pepper"),
    ("basil", "basil"),
    ("corn", "corn")
)
FRUITS = (
    ("apple", "apple"),
    ("banana", "banana"),
    ("lime", "lime"),
    ("lemon", "lemon"),
    ("strawberry", "strawberry"),
    ("orange", "orange"),
    ("pinapple", "pinapple"),
    ("bluberry", "bluberry"),
    ("raisin", "raisin"),
    ("coconut", "coconut"),
    ("grape", "grape"),
    ("peach", "peach"),
    ("mango", "mango"),
    ("pear", "pear"),
    ("cherry", "cherry"),
    ("kiwi", "kiwi"),
    ("date", "date"),
    ("watermelon", "watermelon"),
    ("grapefruit", "grapefruit"),
    ("mandarin", "mandarin"),
    ("plum", "plum"),
    ("raspberry", "raspberry"),
    ("blackberry", "blackberry"),
    ("cranberry", "cranberry"),
)
BACKING_AND_GRAINS = (
    ("rice", "rice"),
    ("pasta", "pasta"),
    ("flour", "flour")
)
SWEETENERS = (
    ("sugar", "sugar"),
    ("honey", "honey"),
    ("brown sugar", "brown sugar")
)
SPICES = (
    ("vanilla", "vanilla"),
    ("cinnamon", "cinnamon"),
    ("garlic powder", "garlic powder"),
    ("paprika", "paprika")

)
MEATS = (
    ("ckicken breast", "ckicken breast"),
    ("ground beaf", "ground beaf"),
    ("sausage", "sausage")
)
FISH_AND_SEAFOOD = (
    ("salmon", "salmon"),
    ("canned tuna", "canned tuna"),
    ("tilapia", "tilapia")
)
CONDIMENTS = (
    ("ketchup", "ketchup"),
    ("mayonnaise", "mayonnaise"),
    ("mustard", "mustard"),
    ("soy sause", "soy sause"),
    ("balsamic", "balsamic"),
)
BEVERAGES = (
    ("coffee", "coffee"),
    ("orange juice", "orange juice"),
    ("tae", "tae"),
    ("green tae", "green tae"),
    ("apple juice", "apple juice"),
)
LEGUMES = (
    ("grean beans", "grean beans"),
    ("peas", "peas"),
    ("lentil", "lentil"),
    ("chickpea", "chickpea"),
)
NUTS = (
    ("peanut butter", "peanut butter"),
    ("almond", "almond"),
    ("pecan", "pecan"),
    ("walnut", "walnut"),
    ("peanut", "peanut"),
)
OIL = (
    ("olive oil", "olive oil"),
    ("vegetable oil", "vegetable oil"),
    ("sunflower oil", "sunflower oil"),
    ("peanut oil", "peanut oil"),
)


class chooseIngredientsForm(forms.Form):
    dairy = forms.MultipleChoiceField(
        required=False,
        label="dairy",
        choices=DAIRY,
        widget=forms.CheckboxSelectMultiple(),
    )
    vegetables = forms.MultipleChoiceField(
        required=False,
        label="vegetables",
        choices=VEGETABLES,
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


