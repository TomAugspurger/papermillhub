import os
from traitlets import config

c = config.get_config()

# Register the papermillhub service with JupyterHub
c.JupyterHub.services = [
    {
        "name": "papermillhub",
        "admin": True,
        "url": "http://127.0.0.1:5000",
        "command": ["papermillhub", "--config", __file__],
        "api_token": "super-secret"
    }
]
c.JupyterHub.service_tokens = {"super-secret": "papermillhub"}

# Setup authenticator and spawners
c.JupyterHub.admin_access = True  # Service needs to access user servers.
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'

c.JupyterHub.spawner_class = "jupyterhub.spawner.SimpleLocalProcessSpawner"
c.SimpleLocalProcessSpawner.home_dir_template = os.getcwd()
c.Spawner.default_url = "/lab"
c.JupyterHub.cookie_secret_file = '/home/taugspurger/jupyterhub_cookie_secret'


# --------------------------
# PapermillHub configuration
c.PapermillHub.db_url = "sqlite:///papermillhub.db"
c.PapermillHub.db_debug = True
