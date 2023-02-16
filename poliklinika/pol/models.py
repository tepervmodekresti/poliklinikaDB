from django.db import models


class Napravlenie(models.Model):
    """Направления"""
    name = models.CharField("Направление", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Vrach(models.Model):
    """Врачи"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"


class Procedure(models.Model):
    """Процедуры"""
    title = models.CharField("Название", max_length=100)
    # tagline = models.CharField("Специальность", max_length=100, default='')
    description = models.TextField("Описание")
    budget = models.PositiveIntegerField("Стоимость", default=0, help_text="указывать сумму в рублях")
    napravlenie = models.ForeignKey(
        Napravlenie, verbose_name="Направление", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP aдрес", max_length=15)
    vrach = models.ForeignKey(Vrach, on_delete=models.CASCADE, verbose_name="С лучшим рейтингом")
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, verbose_name="С лучшим рейтингом")

    def __str__(self):
        return f"{self.vrach}-{self.procedure}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    vrach = models.ForeignKey(Vrach, verbose_name="Врач", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.vrach}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
