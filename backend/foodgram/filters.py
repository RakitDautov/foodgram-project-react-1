import django_filters as filters

from .models import Ingredient, Recipe, Tag, Favorite


class RecipeFilter(filters.FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ['author', 'tags', ]


class FavoriteFilter(filters.FilterSet):
    is_favorited = filters.BooleanFilter(method='get_is_favorited')

    class Meta:
        model = Recipe
        fields = ['author', 'is_favorited']

    def get_is_favorited(self, queryset, name, value):
        user = self.request.user
        if value:
            return Favorite.objects.filter(user=user)
        return False


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='startswith')

    class Meta:
        model = Ingredient
        fields = ('name', )
