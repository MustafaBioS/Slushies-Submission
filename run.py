from app import create_app
from routes import register_routes

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)