#run admin app

from admin_app import create_app as app_admin_create_app
admin = app_admin_create_app()

if __name__ == '__main__':
    admin.run(debug=True, host='0.0.0.0', use_reloader=False)