from backend_app import create_app as app_backend_app_create_app
backend_app = app_backend_app_create_app()

if __name__ == '__main__':
    backend_app.run(debug=True, host='0.0.0.0', use_reloader=False)