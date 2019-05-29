from flask import Flask
from flask_restful import Resource , Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self,name=None):
        buff = None
        if(name!=None):
            buff = {'student':name}
        else:
            buff = {'hello':'world'}
        return buff

#http://localhost:5000/
"""
#http://localhost:5000/
{
    "hello":"world"
}
"""
#http://localhost:5000/student/bob
"""
{
"student": "bob"
}
"""

api.add_resource(Student,'/','/student/<string:name>')

if(__name__=='__main__'):
    app.run(port=5000,debug=True)