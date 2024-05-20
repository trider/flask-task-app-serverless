# blueprints/documented_endpoints/__init__.py
from flask import Blueprint
from flask_restplus import Api
from blueprints import namespace as flask_task_app_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='Flask RESTplus Demo',
    version='1.0',
    description='Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation',
    doc='/doc'
)

api_extension.add_namespace(flask_task_app_ns)