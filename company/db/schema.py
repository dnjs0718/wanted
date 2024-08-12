from tortoise import fields
from tortoise.models import Model

from common.db.schema import BaseMixin


class Company(Model, BaseMixin):
    name = fields.CharField(max_length=255)
    
    class Meta:
        table = 'companies'


class Language(Model, BaseMixin):
    full_name = fields.CharField(max_length=255)
    short_name = fields.CharField(max_length=100)
    
    class Meta:
        table = 'languages'
        

class CompanyLanguage(Model, BaseMixin):
    company = fields.ForeignKeyField(model_name="models.Company", on_delete=fields.CASCADE, related_name='company_languages')
    language = fields.ForeignKeyField(model_name="models.Language", on_delete=fields.CASCADE, related_name='company_languages')
    name = fields.CharField(max_length=255)
    
    class Meta:
        table = 'company_languages'
        

class Tag(Model, BaseMixin):
    name = fields.CharField(max_length=100)
    
    class Meta:
        table = 'tags'


class CompanyTag(Model, BaseMixin):
    company = fields.ForeignKeyField(model_name="models.Company", on_delete=fields.CASCADE, related_name='company_tags')
    tag = fields.ForeignKeyField(model_name="models.Tag", on_delete=fields.CASCADE, related_name='company_tags')
    
    class Meta:
        table = 'company_tags'


class TagLanguage(Model, BaseMixin):
    tag = fields.ForeignKeyField(model_name="models.Tag", on_delete=fields.CASCADE, related_name='tag_languages')
    language = fields.ForeignKeyField(model_name="models.Language", on_delete=fields.CASCADE, related_name='tag_languages')
    name = fields.CharField(max_length=255)
    
    class Meta:
        table = 'tag_languages'