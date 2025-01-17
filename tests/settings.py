SECRET_KEY = "some_secret_key"

USE_TZ = True

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "rest_framework",
    "drf_standardized_errors",
    "tests",
)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

MIDDLEWARE_CLASSES = ("django.middleware.common.CommonMiddleware",)

PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)

ROOT_URLCONF = "tests.urls"

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_SCHEMA_CLASS": "drf_standardized_errors.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "API",
    "DESCRIPTION": "Amazing API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "ENUM_NAME_OVERRIDES": {
        "ValidationErrorEnum": "drf_standardized_errors.openapi_serializers.ValidationErrorEnum.values",
        "ClientErrorEnum": "drf_standardized_errors.openapi_serializers.ClientErrorEnum.values",
        "ServerErrorEnum": "drf_standardized_errors.openapi_serializers.ServerErrorEnum.values",
        "ErrorCode401Enum": "drf_standardized_errors.openapi_serializers.ErrorCode401Enum.values",
        "ErrorCode403Enum": "drf_standardized_errors.openapi_serializers.ErrorCode403Enum.values",
        "ErrorCode404Enum": "drf_standardized_errors.openapi_serializers.ErrorCode404Enum.values",
        "ErrorCode405Enum": "drf_standardized_errors.openapi_serializers.ErrorCode405Enum.values",
        "ErrorCode406Enum": "drf_standardized_errors.openapi_serializers.ErrorCode406Enum.values",
        "ErrorCode415Enum": "drf_standardized_errors.openapi_serializers.ErrorCode415Enum.values",
        "ErrorCode429Enum": "drf_standardized_errors.openapi_serializers.ErrorCode429Enum.values",
        "ErrorCode500Enum": "drf_standardized_errors.openapi_serializers.ErrorCode500Enum.values",
    },
    "POSTPROCESSING_HOOKS": [
        "drf_standardized_errors.openapi_hooks.postprocess_schema_enums"
    ],
}
