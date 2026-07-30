from flask import Flask
from config import Config

import os

def create_app():
    # Explicitly set absolute paths for templates and static folders to support Vercel serverless runtime
    base_dir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')
    
    print("=== DEBUG VERCEL FILESYSTEM ===")
    print("Base dir resolved:", base_dir)
    print("Template dir resolved:", template_dir)
    print("Template dir exists:", os.path.exists(template_dir))
    if os.path.exists(template_dir):
        print("Template dir contents:", os.listdir(template_dir))
        public_dir = os.path.join(template_dir, 'public')
        print("Public template dir exists:", os.path.exists(public_dir))
        if os.path.exists(public_dir):
            print("Public template contents:", os.listdir(public_dir))
    print("================================")
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object(Config)

    # Register Blueprints
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

if __name__ == "__main__":
    app.run(debug=True)

