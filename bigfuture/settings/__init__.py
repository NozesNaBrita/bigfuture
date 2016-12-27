# -*- coding: utf-8 -*-
# Copyright (C) 2016-2017 Maurício Vieira <mauricio@mauriciovieira.net>

import os, sys


try:
    print("Trying import local.py settings...", file=sys.stderr)
    from .local import *
except ImportError:
    print("Trying import dev.py settings...", file=sys.stderr)
    from .dev import *
