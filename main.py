from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video, required arg", required=True)
video_put_args.add_argument("likes", type=str, help="Likes of the video, required arg", required=True)
video_put_args.add_argument("views", type=str, help="Views on the video, required arg", required=True)

videos = {}

def abort_if_not_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video doesnt found!")

def abort_if_already_exist(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with the same id!")

class Video(Resource):
    def get(self, video_id):
        abort_if_not_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_already_exist(video_id)       
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id]

    def delete(self, video_id):
        abort_if_not_exist(video_id)
        del videos[video_id]        
        return '', 204

#add 'HelloWorld' class to the api 'resource'
api.add_resource(Video, '/video/<int:video_id>')

if __name__ == "__main__":
    # debug mode for development purpose
    app.run(debug=True)