from flask_restful import Resource,reqparse
import pymysql
from models.User import User
from werkzeug.security import check_password_hash,generate_password_hash



        
""" Login Resource """
class UserSignInResource(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("username")
        parser.add_argument("password")
        args = parser.parse_args()

        try:
            user = User.find_by_username(args["username"])
            if user and check_password_hash(user["password"],args["password"]):
                return {"status":"success","userId":user["id"]},201
            return {"status":"failed","msg":"Incorrect Email or Password"},400

        except Exception as e:
            print(e)
            return {"status":"failed","msg":"Server Error"},500
            
""" SignUp Resource """
class UserSignUpResource(Resource):

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("username")
        parser.add_argument("password")

        args = parser.parse_args()

        try:
            user = User.find_by_username(args["username"])
            if user:
                return {"status":"failed","msg":"User already exists"},400
           
            User.save(args)
            return {"status":"account created"},200
        except Exception as e:
            print(e)
            return {"status":"failed","msg":"server error"},500