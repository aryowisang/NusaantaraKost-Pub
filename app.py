import os
from flask import Flask, render_template
from config import Config

def home():
    return render_template('templates/index.html')
        
def create_app():
    # Absolute paths required for Vercel serverless runtime
    base_dir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')

    import logging
    logging.basicConfig(level=logging.INFO)
    logging.info("STARTUP DIAGNOSTICS:")
    logging.info(f"  BASE_DIR: {base_dir}")
    logging.info(f"  template_dir: {template_dir}")
    logging.info(f"  template_dir exists: {os.path.exists(template_dir)}")
    if os.path.exists(template_dir):
        logging.info(f"  os.listdir(template_dir): {os.listdir(template_dir)}")

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object(Config)
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True

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

    @app.route('/_debug_templates')
    def debug_templates():
        import os
        from flask import jsonify
        cwd = os.getcwd()
        
        # Build structure walk
        walk_data = {}
        for root, dirs, files in os.walk(cwd):
            # Exclude virtual environment or python cache to keep it clean
            if any(p in root for p in ['venv', '.git', '__pycache__', '.vercel', '_vendor']):
                continue
            rel_path = os.path.relpath(root, cwd)
            walk_data[rel_path] = {
                'dirs': dirs,
                'files': files
            }

        search_paths = []
        if app.jinja_loader and hasattr(app.jinja_loader, 'searchpath'):
            search_paths = app.jinja_loader.searchpath
        elif app.jinja_loader and hasattr(app.jinja_loader, 'loaders'):
            search_paths = [getattr(l, 'searchpath', None) for l in app.jinja_loader.loaders]

        return jsonify({
            'cwd': cwd,
            'template_dir': template_dir,
            'template_dir_exists': os.path.exists(template_dir),
            'jinja_search_paths': search_paths,
            'directory_walk': walk_data,
            '__file__': __file__,
            'env': {k: v for k, v in os.environ.items() if 'KEY' not in k and 'SECRET' not in k and 'PASSWORD' not in k}
        })

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
