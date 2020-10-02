from flask_restful import Resource,reqparse
import pymysql
from models.Account import Account
from storage_security import StorageSecurity

class AccountListResource(Resource):
    
    def get(self):
        try:
            SS = StorageSecurity()
            parser = reqparse.RequestParser()
            parser.add_argument("user")
            args = parser.parse_args()

            accounts = Account.getByUserId(args["user"])
            if accounts and len(accounts)>0:
               """ decrypt the passwords """ 
               for account in accounts:
                   account["password"]=SS.decrypt(account["password"])
               return accounts
            elif accounts and len(accounts)==0:
                return {"msg":"No accounts found"}    
        
        except Exception as e:
            print(e)
            return {"status":"failed","msg":"server error"},500


class CreateAccountResource(Resource):
      
      def post(self):
          try:
              SS = StorageSecurity()
              parser = reqparse.RequestParser()
              parser.add_argument("user")
              parser.add_argument("website")
              parser.add_argument("username")
              parser.add_argument("password")

              args = parser.parse_args()
              print(args)

              #encrypt the password
              args["password"] = SS.encrypt(args["password"])

              Account.save(args)

              return {"status":"success"},200
          except Exception as e:
              print(e)
              return {"status":"failure","msg":"server error"},500

            


