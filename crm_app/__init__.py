#CRM application

from flask import Flask

def create_app():
    app_name = 'crm'
    print ('Application name = {}'.format(app_name))

    app = Flask(__name__, instance_relative_config=True,
                static_folder='/home/flask/project/shared/static', template_folder='/home/flask/project/shared/template')

    @app.route('/')
    def crm():
        return "This is crm panel"

    return app