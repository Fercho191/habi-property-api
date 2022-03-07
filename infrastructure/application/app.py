from flask import Flask

from infrastructure.delivery.web.controller import PropertyController

app = Flask(__name__)
app.register_blueprint(PropertyController.property_bp)

if __name__ == '__main__':
    app.run(debug=True)
