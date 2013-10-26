# """
# Define static webasset bundles.
# """
from flask.ext.assets import Bundle

all_css = Bundle(
	'css/normalize.css',
	'css/main.css',
	'css/map.css',
	filters='cssmin',
	output='build/all.css',
	debug=True
)

# Bundle js libs, except jQuery (loads from CDN) and Modernizr (loads in head).
libs_js = Bundle(
    'js/lib/foundation/*.js',
    filters='uglifyjs',
    output='build/lib.js',
    debug=True
)

# App js
app_js = Bundle(
	'js/login_handler.js',
	'js/facebook_init.js',
	filters='uglifyjs',
	output='build/app.js',
	debug=True
)