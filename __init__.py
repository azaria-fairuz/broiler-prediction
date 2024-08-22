# import dependancies
from flask import Flask, jsonify

# import helper
from App.Helpers import DirectoryHelper

# import routes
from Routes import web as web_routes, api as api_routes

# initiate flask app
working_dir = DirectoryHelper.get_curr_work_dir()
app = Flask(__name__, template_folder=working_dir['templates_dir'], static_url_path='', static_folder=working_dir['public_dir'])

# register blueprints routes
app.register_blueprint(api_routes.api, url_prefix='/api')
app.register_blueprint(web_routes.web, url_prefix='/')

# run flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)