from django.db import models


# Create your models here.


class Material(models.Model):
    """Класс содержащий тип материала и т.д."""
    MAT_TYPE = (('Copper', 'Медь'),
                ('Brass', 'Латунь'),
                ('Steel', 'Сталь'),
                ('Cast iron', 'Чугун'),
                ('Stainless Steel', 'Нержавеющая Сталь'),
                ('Carbon Steel', 'Углеродистая Сталь'),
                ('Instrumental Steel', 'Инструментальная Сталь'),
                ('PFE', 'Фторопласт'),
                ('Nylon', 'Капролон'),
                ('FR-4', 'Стеклотекстолит'),
                ('Zedex', 'Zedex'),
                ('Textolite', 'Текстолит'),
                ('Aluminium', 'Алюминий')
                )

    mat_type = models.CharField(
        max_length=20,
        choices=MAT_TYPE,
        blank=True,
        default='Steel')
    mat_name = models.CharField(max_length=40, unique=True, primary_key=True)
    mat_gost = models.CharField(max_length=40, unique=False)
    density = models.IntegerField()

    class Meta:
        ordering = ['mat_type']

    def __str__(self):
        """Возвращает название материала и его ГОСТ"""
        return '%s \n %s' % (self.mat_name, self.mat_gost)


class Relative(models.Model):
    """Список серийных изделий"""
    rel = models.CharField(max_length=10, unique=True, primary_key=True)

    class Meta:
        ordering = ['rel']

    def __str__(self):
        """В случае обращения возвращает номер чертежа"""
        return self.rel


class Notice(models.Model):
    """Список извещений и их номеров"""
    notice = models.CharField(max_length=10, unique=True, primary_key=True)
    notice_date = models.DateField()

    def __str__(self):
        """Возвращает название материала и его ГОСТ"""
        return "%s от %s" % (self.notice, self.notice_date)


class TechProp(models.Model):
    """Класс определяющий основные свойства деталей - название, номер, материал, метод изготовления, трудоемкость,
    ссылку на чертеж и т.д."""

    draw_num = models.CharField(max_length=30, unique=True, primary_key=True, help_text='Введите номер чертежа',
                                verbose_name='Номер чертежа')  # Номер чертежа - базовый тип

    name = models.CharField(max_length=15, unique=False, help_text='Введите название детали',
                            verbose_name='Название детали')
    draw_url = models.URLField(verbose_name='Ссылка на чертеж', blank=True)

    """Типы обработки"""
    TRUE_FALSE_CHOICES = ((True, 'Да'), (False, 'Нет'))

    punchable = models.BooleanField(verbose_name='ШТ')  # Деталь изготавливается на штамповке
    machinable = models.BooleanField(verbose_name='ИП')  # Деталь изготавливается в ИП ПКО
    solder = models.BooleanField(verbose_name='СП')  # Спекание
    assembly = models.BooleanField(verbose_name='СКД')  # Участок сборки
    galvan = models.BooleanField(verbose_name='ГАЛ')  # Участок гальваники

    """Подразделение заказчик"""
    subdivision_ch = (('MV1', 'ПКГ'), ('MV2', 'ЛКГ'), ('QR1', 'ПКРиФ'), ('QR2', 'ПКЭ'), ('PKO', 'ПКиО'))
    subdivision = models.CharField(
        max_length=5,
        choices=subdivision_ch,
        blank=True,
        default=None,
        verbose_name='Заказчик')

    """Параметры ссылающиеся на другие модели"""
    # laboriousness = models.ForeignKey('Laboriousness',                      # Кавычки используются когда ссылка идет на класс, который опрелен ниже
    # on_delete=models.CASCADE, null=True)  # Трудоемкость.

    """Класс определяющий тип приемки - ВП, ОТК"""
    ACCEPT_TYPE = (('VP', 'ВП(5)'), ('OTK', 'ОТК(1)'))
    accept = models.CharField(
        max_length=20,
        choices=ACCEPT_TYPE,
        blank=True,
        default='O-vi')  # Приемка ВП/ОТК - берем из др. класса

    """Типы покрытия на деталях"""
    COATING_TYPE = (('O-vi', 'Олово-висмут'),
                    ('NPb', 'Никель полублестящий'),
                    ('Ag', 'Серебро'),
                    ('None', 'б/п'),
                    )

    coating = models.CharField(
        max_length=20,
        choices=COATING_TYPE,
        blank=True,
        default='O-vi',
        verbose_name='Покрытие')  # Тип покрытия из отдельной таблицы

    draw_mat = models.ForeignKey(Material,
                                 on_delete=models.CASCADE, null=True,
                                 verbose_name='Материал')  # Чертежный материал. Берем из отдельной таблицы.
    notice = models.ForeignKey(Notice,
                               on_delete=models.CASCADE, null=True, blank=True)  # Номер извещения + дата

    """Примечания к детали"""

    class Meta:
        ordering = ['subdivision', 'name', 'draw_num']

    def __str__(self):
        """В случае обращения возвращает номер чертежа"""
        return self.draw_num


"""
class Laboriousness(models.Model):
    draw_num = models.OneToOneField(TechProp, on_delete=models.CASCADE)  # Перенос номера из TechProp

    laboriousness = models.CharField(max_length=10)

    class Meta:
        ordering = ['draw_num']

    def __str__(self):

        return self.laboriousness
"""