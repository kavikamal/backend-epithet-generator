def configure_app():
    import os
    import dotenv
    from flask import Flask
    PROJECT_ROOT = os.path.dirname('.')
    dotenv.load_dotenv(os.path.join(PROJECT_ROOT, '.env'))
    return Flask(__name__)


app = configure_app()
