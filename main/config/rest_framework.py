REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S%Z",
    "DATETIME_INPUT_FORMAT": "%Y-%m-%d %H:%M:%S%Z",
    "DEFAULT_PAGINATION_CLASS": "apps.common.utils.pagination.CustomPagination",
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
}
