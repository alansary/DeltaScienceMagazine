LOCAL = False

if LOCAL:
    from .local import *
else:
    from .production import *