from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast
from handlemanuscript import FindQRCode
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('pngUrls', type=str)


class HandleManuscript(Resource):
    def post(self):
        args = parser.parse_args()
        resData = {}
        pngDicts = ast.literal_eval(args.pngUrls)

        for key in pngDicts:
            res = FindQRCode.findqrcode(pngDicts[key])
            resData[str(key)] = str(res)
        return resData


api.add_resource(HandleManuscript, '/handleManuscript')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

