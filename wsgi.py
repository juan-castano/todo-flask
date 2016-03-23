import os
import sys

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from app import app as application


virtenv = os.path.expanduser('~') + '/flask/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

try:
    exec(open(virtualenv).read(), dict(__file__=virtualenv))
except IOError:
    pass

sys.path.append(os.path.expanduser('~'))
sys.path.append(os.path.expanduser('~') + '/ROOT/')

"""
application = DispatcherMiddleware(create_app(), {
    '/api': create_api()
})
"""

if __name__ == "__main__":
    run_simple(
        '0.0.0.0',
        5000,
        application,
        use_reloader=True,
        use_debugger=True
    )
