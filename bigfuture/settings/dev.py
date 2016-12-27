# -*- coding: utf-8 -*-
# Copyright (C) 2016-2017 Maurício Vieira <mauricio@mauriciovieira.net>

# Inspiration: https://github.com/taigaio/taiga-back/blob/e215fa41470e74fbd100ecacdd55d98b47a2b55d/settings/common.py

from .base import *

DEBUG = True

TEMPLATES[0]["OPTIONS"]['context_processors'] += "django.template.context_processors.debug"
