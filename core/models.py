from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError
from django.db import models


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Դուք կարող եք ստեղծել միայն մեկ" % model.__name__)


class SectionGeneral(models.Model):
    name_hy = models.CharField(max_length=30, blank=True, db_index=True, verbose_name='Անուն Ազգանուն (hy)')
    name_ru = models.CharField(max_length=30, blank=True, db_index=True, verbose_name='Անուն Ազգանուն (ru)')
    name_en = models.CharField(max_length=30, blank=True, db_index=True, verbose_name='Անուն Ազգանուն (en)')
    info_hy = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Պաշտոն և այլն (hy)')
    info_ru = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Պաշտոն և այլն (ru)')
    info_en = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Պաշտոն և այլն (en)')
    phone = models.CharField(max_length=20, db_index=True, verbose_name='Հեռախոսահամար')
    img = models.ImageField(upload_to='general', verbose_name='Նկար')

    class Meta:
        verbose_name = 'Բժշկի անձնական տվյալներ'
        verbose_name_plural = 'Բժշկի անձնական տվյալներ'

    def __str__(self):
        return self.name_hy

    def clean(self):
        validate_only_one_instance(self)


class GeneralServices(models.Model):
    name_hy = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Ծառայության անուն (hy)')
    name_ru = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Ծառայության անուն (ru)')
    name_en = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Ծառայության անուն (en)')
    body_hy = RichTextField(max_length=7000, blank=True, verbose_name='Ծառայության մասին (hy)')
    body_ru = RichTextField(max_length=7000, blank=True, verbose_name='Ծառայության մասին (ru)')
    body_en = RichTextField(max_length=7000, blank=True, verbose_name='Ծառայության մասին (en)')
    img = models.ImageField(upload_to='services', verbose_name='Ծառայության նկար')

    class Meta:
        verbose_name = 'Գովազդային ծառայություն'
        verbose_name_plural = 'Գովազդային ծառայություն'

    def __str__(self):
        return self.name_hy

    def clean(self):
        validate_only_one_instance(self)


class Services(models.Model):
    name_hy = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Ծառայության անուն (hy)')
    name_ru = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Ծառայության անուն (ru)')
    name_en = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Ծառայության անուն (en')
    body_hy = RichTextField(max_length=3000, blank=True, verbose_name='Ծառայության մասին (hy)')
    body_ru = RichTextField(max_length=3000, blank=True, verbose_name='Ծառայության մասին (ru)')
    body_en = RichTextField(max_length=3000, blank=True, verbose_name='Ծառայության մասին (en)')
    img = models.ImageField(upload_to='services', verbose_name='Ծառայության նկար')

    class Meta:
        verbose_name = 'Ծառայություններ'
        verbose_name_plural = 'Ծառայություններ'

    def __str__(self):
        return self.name_hy


class AboutMe(models.Model):
    img = models.ImageField(upload_to='about', verbose_name='Մեր մասին նկար')
    body_l_hy = RichTextField(max_length='3000', blank=True, verbose_name='Մեր մասին տեքստ (hy) ձախ')
    body_l_ru = RichTextField(max_length='3000', blank=True, verbose_name='Մեր մասին տեքստ (ru) ձախ')
    body_l_en = RichTextField(max_length='3000', blank=True, verbose_name='Մեր մասին տեքստ (en) ձախ')
    body_r_hy = RichTextField(max_length='3000', blank=True, verbose_name='Մեր մասին տեքստ (hy) աջ')
    body_r_ru = RichTextField(max_length='3000', blank=True, verbose_name='Մեր մասին տեքստ (ru) աջ')
    body_r_en = RichTextField(max_length='3000', blank=True, verbose_name='Մեր մասին տեքստ (en) աջ')

    class Meta:
        verbose_name = 'Բժշկի մասին'
        verbose_name_plural = 'Բժշկի մասին'

    def __str__(self):
        return self.body_l_hy

    def clean(self):
        validate_only_one_instance(self)


class Works(models.Model):
    img = models.ImageField(upload_to='works/%Y/%m/%d', blank=True, verbose_name='Մեր գործերը նկար')
    url = models.CharField(max_length=1000, blank=True, verbose_name='Մեր գործերը լինք')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Կատարված աշխատանք'
        verbose_name_plural = 'Կատարված աշխատանքներ'


class Review(models.Model):
    content_hy = models.TextField(max_length=4000, blank=True, verbose_name='Ակնարկներ (hy)')
    content_ru = models.TextField(max_length=4000, blank=True, verbose_name='Ակնարկներ (ru)')
    content_en = models.TextField(max_length=4000, blank=True, verbose_name='Ակնարկներ (en)')
    name_hy = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Անուն Ազգանուն (hy)')
    name_ru = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Անուն Ազգանուն (ru)')
    name_en = models.CharField(max_length=40, blank=True, db_index=True, verbose_name='Անուն Ազգանուն (en)')
    disease_hy = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Բուժված հիվանդությունը (hy)')
    disease_ru = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Բուժված հիվանդությունը (ru)')
    disease_en = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Բուժված հիվանդությունը (en)')
    published = models.BooleanField(default=False, verbose_name='Հրապարակել')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Կարծիք'
        verbose_name_plural = 'Կարծիքներ'

    def __str__(self):
        return self.name_hy


class Contacts(models.Model):
    phone = models.CharField(max_length=25, db_index=True, verbose_name='Հեռախոսահամա')
    whatsapp = models.CharField(max_length=30, db_index=True, verbose_name='WhatsApp')
    whatsapp_link = models.CharField(max_length=25, db_index=True, verbose_name='WhatsApp (Առանց '+' և բացատի)')
    viber = models.CharField(max_length=30, db_index=True, verbose_name='Viber')
    viber_link = models.CharField(max_length=25, db_index=True, verbose_name='Viber (Առանց '+' և բացատի)')
    fb = models.CharField(max_length=100, db_index=True, verbose_name='Facebook')
    mail = models.CharField(max_length=50, db_index=True, verbose_name='Mail')
    address_hy = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Հասցե (hy)')
    address_ru = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Հասցե (ru)')
    address_en = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Հասցե (en)')

    class Meta:
        verbose_name = 'Կոնտակտ'
        verbose_name_plural = 'Կոնտակտներ'

    def __str__(self):
        return self.phone

    def clean(self):
        validate_only_one_instance(self)


class Information(models.Model):
    name_hy = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Հիվանդության անունը (hy)')
    name_ru = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Հիվանդության անունը (ru)')
    name_en = models.CharField(max_length=100, blank=True, db_index=True, verbose_name='Հիվանդության անունը (en)')
    info_hy = RichTextUploadingField(blank=True, verbose_name='Հիվանդությունների մասին և այլն (hy)')
    info_ru = RichTextUploadingField(blank=True, verbose_name='Հիվանդությունների մասին և այլն (ru)')
    info_en = RichTextUploadingField(blank=True, verbose_name='Հիվանդությունների մասին և այլն (en)')

    class Meta:
        verbose_name = 'Հիվանդությունների մասին և այլն'
        verbose_name_plural = 'Հիվանդությունների մասին և այլն'

    def __str__(self):
        return self.name_hy

TIME_CHOICES = [
    ('10:00-10:30', '10:00-10:30'),
    ('10:30-11:00', '10:30-11:00'),
    ('11:00-11:30', '11:00-11:30'),
    ('11:30-12:00', '11:30-12:00'),
    ('12:00-12:30', '12:00-12:30'),
    ('12:30-13:00', '12:30-13:00'),
    ('13:00-13:30', '13:00-13:30'),
    ('13:30-14:00', '13:30-14:00'),
    ('14:00-14:30', '14:00-14:30'),
    ('14:30-15:00', '14:30-15:00'),
    ('15:00-15:30', '15:00-15:30'),
    ('15:30-16:00', '15:30-16:00'),
    ('16:00-16:30', '16:00-16:30'),
    ('16:30-17:00', '16:30-17:00'),
]


class CheckedDate(models.Model):
    date = models.DateField(auto_now_add=False, blank=True, verbose_name='Ամիս ամսաթիվ')

    class Meta:
        verbose_name = 'Աշխատանքային օր'
        verbose_name_plural = 'Աշխատանքային օրեր'

    def __str__(self):
        return str(self.date)

class CheckedTime(models.Model):
    TIME_CHOICES = [
        ('10:00-10:30', '10:00-10:30'),
        ('10:30-11:00', '10:30-11:00'),
        ('11:00-11:30', '11:00-11:30'),
        ('11:30-12:00', '11:30-12:00'),
        ('12:00-12:30', '12:00-12:30'),
        ('12:30-13:00', '12:30-13:00'),
        ('13:00-13:30', '13:00-13:30'),
        ('13:30-14:00', '13:30-14:00'),
        ('14:00-14:30', '14:00-14:30'),
        ('14:30-15:00', '14:30-15:00'),
        ('15:00-15:30', '15:00-15:30'),
        ('15:30-16:00', '15:30-16:00'),
        ('16:00-16:30', '16:00-16:30'),
        ('16:30-17:00', '16:30-17:00'),
    ]
    date = models.ForeignKey('CheckedDate', on_delete=models.CASCADE)
    time = models.CharField(max_length=12, choices=TIME_CHOICES, verbose_name='Ժամ')

    class Meta:
        verbose_name = 'Աշխատանքային ժամ'
        verbose_name_plural = 'Աշխատանքային ժամեր'

    def __str__(self):
        return self.time




# TIME_CHOICES = [
#     ('10:00-10:30', '10:00-10:30'),
#     ('10:30-11:00', '10:30-11:00'),
#     ('11:00-11:30', '11:00-11:30'),
#     ('11:30-12:00', '11:30-12:00'),
#     ('12:00-12:30', '12:00-12:30'),
#     ('12:30-13:00', '12:30-13:00'),
#     ('13:00-13:30', '13:00-13:30'),
#     ('13:30-14:00', '13:30-14:00'),
#     ('14:00-14:30', '14:00-14:30'),
#     ('14:30-15:00', '14:30-15:00'),
#     ('15:00-15:30', '15:00-15:30'),
#     ('15:30-16:00', '15:30-16:00'),
#     ('16:00-16:30', '16:00-16:30'),
#     ('16:30-17:00', '16:30-17:00'),
# ]
#
#
# class TimeChoices(models.Model):
#     time = models.CharField(max_length=12, choices=TIME_CHOICES, verbose_name='Ժամ')
#     date = models.DateField(auto_now_add=False, blank=True, verbose_name='Ամիս ամսաթիվ')
#
#     class Meta:
#         verbose_name = 'Աշխատանքային ժամ'
#         verbose_name_plural = 'Աշխատանքային ժամեր'
#
#     def __str__(self):
#         return self.date





