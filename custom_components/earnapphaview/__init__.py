""" Init """
""" import """
from earnapp import earnapp

""" import HA """
import voluptuous as vol
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType
from homeassistant.config_entries import ConfigEntry
from datetime import timedelta

""" DOMAIN """
DOMAIN = "EarnAppHAview"

""" const """
from .const import (
    __name__,
    __version__,
    CONF_UP_INTERVAL,
)
PLATFORMS = ["sensor"]

import logging
_LOGGER = logging.getLogger(__name__)

""" Schema """
EARNAPP_SCHEMA = vol.Schema(
    {
        vol.Required(token): cv.string,
    }
)


CONFIG_SCHEMA = vol.Schema(
    {vol.Optional(DOMAIN): EARNAPP_SCHEMA}, extra=vol.ALLOW_EXTRA
)
