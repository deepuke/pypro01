from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# class 'HellowWorld' inherit from 'Resource'
class HelloWorld(Resource):
    # override the get method
    def get(self):
        #python library [json in javascript]
        return {'hello' : 'Hello world'}
    # override the post method
    def post(self):
        return {'data': 'Posted'}
    


class PassingParams(Resource):
    def get(self, name, age):
        return {'name':name, 'age':age}

#add 'HelloWorld' class to the api 'resource'
api.add_resource(HelloWorld, '/helloworld')
api.add_resource(PassingParams, '/pp/<string:name>/<int:age>') 

if __name__ == "__main__":
    # debug mode for development purpose
    app.run(debug=True)