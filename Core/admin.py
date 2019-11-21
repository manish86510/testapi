from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'modified_on')

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        model_fields = []
        default_fields = ['created_on', 'created_by', 'modified_on', 'modified_by', 'deleted_on', 'deleted_by',
                          'is_active']

        for field in model._meta.fields:

            if field.name not in default_fields and not field.primary_key:
                model_fields.append(field.name)

        self.fieldsets = (
            (
                None, {
                    'fields': model_fields
                }
            ),
            (
                'Core', {
                    'fields': default_fields
                }
            )
        )

