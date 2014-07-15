import os


TORNADO = {
    'debug': True,
    'static_path': os.path.join(os.path.dirname(__file__), '..', 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), '..', 'templates'),
    'cookie_secret': 'b722aa661f45e3f793bdd13eb5ec83b7',
    'login_url': '/auth/login/',
    'domain_name': 'localhost',
    'port': 5000,
    'xsrf_cookies': True,
    'autoescape': None,

}


MONGO = {
    'name': 'randomizer-dev',
    'options': {}
}