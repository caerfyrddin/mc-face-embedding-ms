from flask import Blueprint, request
from app.mc_face_embedding_ms.domain.worker.face_embedding_worker import FaceEmbeddingWorker

mc_face_embedding_ms = Blueprint(
    'mc_face_embedding_ms',
    __name__,
    url_prefix = '/face-embedding/'
)

@mc_face_embedding_ms.route('/', methods = [ 'GET' ])
def home():
    return 'OK'

@mc_face_embedding_ms.route('/get-face-embedding', methods = [ 'GET' ])
def get_face_embedding():
    path = request.args['path']
    rect_top = request.args['rect_top']
    rect_right = request.args['rect_right']
    rect_bottom = request.args['rect_bottom']
    rect_left = request.args['rect_left']
    worker = FaceEmbeddingWorker(path, int(rect_top), int(rect_right), int(rect_bottom), int(rect_left))
    embedding = worker.get_face_embedding()
    response = {
        "face_embedding": embedding
    }
    return response