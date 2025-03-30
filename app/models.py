from app import db

class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key = True) # Unique ID for each task
    task = db.Column(db.String(100), nullable = False)
    status = db.Column(db.Boolean, default = False)
    # This method is used to convert database object to dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "task": self.task,
            "status": self.status
        }