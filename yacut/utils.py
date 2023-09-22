import random
import string

from .models import URLMap
from settings import DEFAULT_LINK_LENGHT


def get_unique_short_id():
    source_symbols = string.ascii_letters + string.digits
    short_link = ''.join(random.choice(source_symbols)
                         for __ in range(DEFAULT_LINK_LENGHT))
    if URLMap.query.filter_by(short=short_link).first():
        return get_unique_short_id()
    return short_link
