# """
# Define static webasset bundles.
# """
from flask.ext.assets import Bundle

all_css = Bundle(
	'css/normalize.css',
	'css/main.css',
	'css/foundation.css',
	'css/app.css',
	'css/map.css',
	filters='cssmin',
	output='build/all.css',
	debug=True
)

# Bundle js libs, except jQuery (loads from CDN) and Modernizr (loads in head).
lib_js = Bundle(
    'js/lib/foundation/foundation.js',
    filters='uglifyjs',
    output='build/lib.js',
    debug=True
)

# App js
app_js = Bundle(
	'js/app_base.js',
	'js/login_handler.js',
	'js/facebook_init.js',
	'js/map.js',
	# filters='uglifyjs',
	output='build/app.js',
	debug=True
)