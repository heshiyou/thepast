#-*- coding:utf-8 -*-

from flask import Flask 

#-- create app --
app = Flask(__name__)
app.config.from_object("past.config")

##-- register blueprint --
from past.visual import blue_print as visual_bp
app.register_blueprint(visual_bp, url_prefix="/visual")

import view

from utils import filters
from utils import wrap_long_line
from utils import markdownize

app.jinja_env.filters['nl2br'] = filters.nl2br
app.jinja_env.filters['linkify'] = filters.linkify
app.jinja_env.filters['html_parse'] = filters.html_parse
app.jinja_env.filters['wrap_long_line'] = wrap_long_line
app.jinja_env.filters['markdownize'] = markdownize
