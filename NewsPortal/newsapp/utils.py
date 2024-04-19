from .models import *
from django.db.models import Count


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        # {'title': "Войти", 'url_name': 'login'},
        ]

#    _____ вариант исчезновения "Добавить статью" из меню для неавторизованного пользователя ___


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        # cats = Category.objects.order_by('name') # отображение всех категорий
        cats = Category.objects.annotate(Count('post')).order_by(
            'name')  # для исчезновения пустых категорий

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context

#    _____ вариант без исчезновения "Добавить статью" из меню для неавторизованного пользователя ___

# class DataMixin:
#     paginate_by = 3
#
#     def get_user_context(self, **kwargs):
#         context = kwargs
#         cats = Category.objects.all()
#         context['menu'] = menu
#         context['cats'] = cats
#         if 'cat_selected' not in context:
#             context['cat_selected'] = 0
#         return context
