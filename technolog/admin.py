from django.contrib import admin

# Register your models here.

from .models import Material, Relative, Notice, TechProp


# Minimal registration of Models.
# admin.site.register(Material)
# admin.site.register(Relative)
# admin.site.register(Notice)
# admin.site.register(TechProp)


class TechPropAdmin(admin.ModelAdmin):
    """Определяем класс админки для основного экрана
    с деталями основного производства
    Выводим список деталей и их свойства. Добавляем фильтр для отбора"""
    list_display = ('draw_num',
                    'name',
                    'subdivision',
                    'draw_mat',
                    'coating',
                    'punchable',
                    'machinable',
                    'solder',
                    'assembly',
                    'galvan'
                    )

    # На случай добавления изменяемых полей

    list_filter = ('subdivision', 'punchable', 'machinable', 'solder', 'assembly', 'galvan')


admin.site.register(TechProp, TechPropAdmin)


class NoticeAdmin(admin.ModelAdmin):
    """Определяем класс админки"""
    pass


admin.site.register(Notice, NoticeAdmin)


class RelativeAdmin(admin.ModelAdmin):
    """Определяем класс админки"""
    pass


admin.site.register(Relative, RelativeAdmin)


class MaterialAdmin(admin.ModelAdmin):
    """Определяем класс админки"""
    pass

admin.site.register(Material, MaterialAdmin)


