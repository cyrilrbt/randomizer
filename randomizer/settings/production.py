import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=5000)
args = parser.parse_args()
port = args.port


TORNADO = {
    'debug': False,
    'static_path': os.path.join(os.path.dirname(__file__), '..', 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), '..', 'templates'),
    'cookie_secret': 'b722aa661f45e3f793bdd13eb5ec83b7',
    'login_url': '/auth/login/',
    'domain_name': 'youtube-playlists.67labs.com',
    'port': port,
    'xsrf_cookies': True,
    'autoescape': None,

}


MONGO = {
    'name': 'randomizer',
    'options': {}
}