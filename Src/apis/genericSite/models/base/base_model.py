import uuid

from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    disabled_at = models.DateTimeField(null=True, blank=True)
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
    def patch(self, active: bool, *args, **kwargs):
        if active is not None:
            self.disabled_at = None if active else timezone.now()
        self.save(*args, **kwargs)

    class Meta:
        abstract = True