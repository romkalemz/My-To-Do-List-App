from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True) # Unique ID for each task
    task = db.Column(db.String(100), nullable = False)
    status = db.Column(db.Boolean, default = False)
    # This method is used to convert Python dict to JSON for responses
    def to_dict(self):
        return {
            "id": self.id,
            "task": self.task,
            "status": self.status
        }