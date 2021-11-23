from crm_app import create_app as app_crm_app_create_app
crm_app = app_crm_app_create_app()

if __name__ == '__main__':
    crm_app.run(debug=True, host='0.0.0.0', use_reloader=False)