from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(500))
    short = db.Column(db.String(16))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('redirect_view', short=self.short,
                               _external=True)
        )
