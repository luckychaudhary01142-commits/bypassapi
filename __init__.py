from .adlink import Adlink
from .gplinks import GPLinks
from .ouo import Ouo
from .softurl import SoftUrl
from .generic_redirect import GenericRedirect
from .smart_fallback import SmartFallback

PLUGINS = [
    Adlink(),
    GPLinks(),
    Ouo(),
    SoftUrl(),
    GenericRedirect(),
]

FALLBACK = SmartFallback()

def find_plugin(url: str):
    for p in PLUGINS:
        if p.matches(url):
            return p
    return FALLBACK
