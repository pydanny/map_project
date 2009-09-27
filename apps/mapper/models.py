from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

COLOR_CHOICES = ( 
    ('blue', 'blue'), 
    ('gray', 'gray'),         
    ('green', 'green'),     
    ('red', 'red'), 
    ('yellow', 'yellow'),     
) 

SHAPE_CHOICES = (
    ('circle', 'circle'),
    ('diamond', 'diamond'),
    ('box', 'box'),        
)


# Create your models here.

class BaseModel(models.Model):
    
    title           = models.CharField(_('title'), max_length=200)
    slug            = models.SlugField(_('slug'))
    created_at      = models.DateTimeField(_('created at'), default=datetime.now)
    modified_at     = models.DateTimeField(_('modified at'), default=datetime.now)    
    
    
    class Meta:
        abstract = True
        
    def __unicode__(self):
        return self.title
        
    def _save_helper(self):
        self.modified = datetime.now()
        self.slug = slugify(self.title)

                    
class ApplicationType(BaseModel):
    
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    shape = models.CharField(max_length=20, choices=SHAPE_CHOICES)    
    
    def save(self, force_insert=False, force_update=False):
        self._save_helper()
        super(ApplicationType, self).save(force_insert, force_update)         
    

class Application(BaseModel):
    
    application_type = models.ForeignKey(ApplicationType)

    def save(self, force_insert=False, force_update=False):
        self._save_helper()
        super(Application, self).save(force_insert, force_update)
        
    def pushing(self):
        return [x.going_to for x in self.coming.all() if x]

    def pulling(self):
        return [x.coming_from for x in self.going.all() if x]

        
        
class Relationship(models.Model):

    coming_from = models.ForeignKey(Application, related_name='coming')    
    going_to    = models.ForeignKey(Application, related_name='going')
    

class Mapp(BaseModel):
    description       = models.TextField(_('description'), max_length=200)    
    Application = models.ForeignKey(User, related_name="modified")
    
    def save(self, force_insert=False, force_update=False):
        self._save_helper()
        super(Mapp, self).save(force_insert, force_update)
    