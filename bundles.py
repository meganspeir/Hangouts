# """
# Define static webasset bundles.
# """
from flask.ext.assets import Bundle



# all_css = Bundle(
#     'css/bootstrap.css',
#     'css/bootstrap-responsive.css',
#     filters='cssmin',
#     output='build/all.css'
# )


# Bundle js libs, except jQuery (loads from CDN) and Modernizr (loads in head).
libs_js = Bundle(
    'js/lib/foundation/*.js'
    filters='uglifyjs',
    output='build/lib.js'
)

# app_js = Bundle(
#     Bundle(
#         'js/app/*.coffee',
#         filters='coffeescript',

#         # Note: these can be eliminated once webassets 0.8 is released.
#         output='build/coffee.js',
#         debug=False
#     ),
#     filters='uglifyjs',
#     output='build/app.js'
# )

# app_js = Bundle(
# 	Bundle(
# 		'js/*.coffee',
# 		filters='coffeescript',
# 		output='build/coffee.js',
# 		debug=True
# 	),
# 	filters='uglifyjs',
# 	output='app.js'

# )