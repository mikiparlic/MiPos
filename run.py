#run all

#import dispacher
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

#import apps
from admin_app import create_app as app_admin_create_app
admin = app_admin_create_app()
from backend_app import create_app as app_backend_app_create_app
backend_app = app_backend_app_create_app()
from on_line_app import create_app as app_on_line_app_create_app
on_line_app = app_on_line_app_create_app()
from crm_app import create_app as app_crm_app_create_app
crm_app = app_crm_app_create_app()

#merge apps

app = DispatcherMiddleware(backend_app, {'/admin': admin,
                                         '/online': on_line_app,
                                         '/crm': crm_app})

if __name__ == '__main__':
    run_simple(hostname='0.0.0.0',
               port = 5000,
               application=app,
               use_reloader=True,
               use_debugger=True,
               use_evalex=True)