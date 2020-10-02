from flask import Flask,jsonify
from flask_cors import CORS
from flask_restful import Api,reqparse,Resource

from resources.UserResource import UserSignInResource,UserSignUpResource
from resources.AccountResource import AccountListResource,CreateAccountResource

app = Flask(__name__)
CORS(app)

api = Api(app)

''' User Authentication Routes '''
api.add_resource(UserSignInResource,"/app/user/auth")
api.add_resource(UserSignUpResource,"/app/user")

''' Account Routes '''
api.add_resource(AccountListResource,"/app/sites/list/")
api.add_resource(CreateAccountResource,"/app/sites/")

if __name__=="__main__":
    app.run()