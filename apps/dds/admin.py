from django.contrib import admin

from apps.dds.models import Transaction, Category, Subcategory, Type


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    list_filter = ("type",)
    inlines = [SubcategoryInline]


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("created_at", "type", "category", "value")
    list_filter = ("type", "category")
    readonly_fields = ("created_at", "updated_at")
    fields = (
        "status",
        "type",
        "value",
        "comment",
        "category",
        "created_at",
        "updated_at",
    )


admin.site.register(Type)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory)
admin.site.register(Transaction, TransactionAdmin)
