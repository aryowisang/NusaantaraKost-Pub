from flask import Flask
from config import Config
import os

def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    print("Root path:", app.root_path)
    print("Template folder:", app.template_folder)
    print("Templates exists:", os.path.exists(os.path.join(app.root_path, "templates")))
    print("Public index exists:", os.path.exists(os.path.join(app.root_path, "templates", "public", "index.html")))

    app.config.from_object(Config)

    from routes.public import public_bp
    from routes.admin import admin_bp
    from routes.kamar import admin_kamar_bp
    from routes.penghuni import admin_penghuni_bp
    from routes.sewa import admin_sewa_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(admin_kamar_bp)
    app.register_blueprint(admin_penghuni_bp)
    app.register_blueprint(admin_sewa_bp)

    return app

app = create_app()
