from on_line_app import create_app as app_on_line_app_create_app
on_line_app = app_on_line_app_create_app()

if __name__ == '__main__':
    on_line_app.run(debug=True, host='0.0.0.0', use_reloader=False)