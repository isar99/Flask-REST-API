from flask_smorest import Blueprint, abort
from flask import Flask
from flask.views import MethodView
from ..schema import TagSchema
from ..models.tag import TagModel

from ..db import db

blp = Blueprint("tags", __name__, description="Operations on tag")

@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag

    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        db.session.delete(tag)
        db.session.commit()
        return {"message": "Tag deleted"}, 200

