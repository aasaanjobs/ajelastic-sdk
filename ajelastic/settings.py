import os
from simple_settings import LazySettings

from ajelastic.exceptions import AJElasticSettingsError


_REQUIRED_SETTINGS = [
    "ES_HOST",
    "ES_ENV"
]


def load_settings():
    """
    First checks whether the consuming project is Django project or not (i.e., if DJANGO_SETTINGS_MODULE env is
    specified or not) else reads the project settings path specified in AJ_ELASTIC_CONF env variable.
    :return: Settings object
    """
    try:
        setting_path = os.environ["DJANGO_SETTINGS_MODULE"]
    except KeyError:
        try:
            setting_path = os.environ["AJ_ELASTIC_CONF"]
        except KeyError:
            raise AJElasticSettingsError("Missing env AJ_ELASTIC_CONF")
    settings = LazySettings(setting_path)
    settings_missing = []
    for _ in _REQUIRED_SETTINGS:
        if not hasattr(settings, _):
            settings_missing.append(_)
    if not settings_missing:
        return settings
    # Throw error
    raise AJElasticSettingsError("Missing required settings {}".format(",".join(settings_missing)))
