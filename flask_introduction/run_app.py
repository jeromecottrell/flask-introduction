import os

from _01_simple import app
# from _02_html_inside_view import app
# from _03_template_str_inside_view import app
# from _04_template_outside_view import app
# from _05_basic_routing import app
# from _06_raising_custom_errors import app
# from _07_request_info import app
# from _08_redirects import app
# from _09_simple_database_app import app
# from _10_database_app_template_eng import app
# from _11_database_app_template_conditional import app
# from _12_database_app_with_join import app
# from _13_simple_form_submission import app
# from _14_static_files import app
# from _15_template_inheritance import app


if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
