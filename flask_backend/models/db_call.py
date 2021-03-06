from flask_backend import db


class DBCall(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    account_id = db.Column(db.Integer)

    phone_number = db.Column(db.String)
    timestamp = db.Column(db.DateTime)

    status = db.Column(db.String)  # "pending", "accepted" and "fulfilled"

    def __repr__(self):
        return f"DBCall(id: {self.id}, account_id: {self.account_id}, phone_number: {self.phone_number}, fulfilled: {self.fulfilled})"


