from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from Apparel_app.views.main_view import main_bp
    from Apparel_app.views.recommend_view import recom_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(recom_bp)
    
    return app