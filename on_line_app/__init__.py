#Online app application

from flask import Flask

def create_app():
    app_name = 'on_line_app'
    print ('Application name = {}'.format(app_name))

    app = Flask(__name__, instance_relative_config=True,
                static_folder='/home/flask/project/shared/static', template_folder='/home/flask/project/shared/template')

    @app.route('/')
    def backend():
        return "This is Online application"

    return app