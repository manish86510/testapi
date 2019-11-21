from django.db import models
from .managers import SoftDeletionManager
from django.utils import timezone


class SoftDeleteModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.IntegerField(null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    deleted_by = models.IntegerField(null=True, blank=True, default=None)
    deleted_on = models.DateTimeField(null=True, default=None, blank=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()

