# routers.py

class FeedbackRouter:
    """
    A router to control all database operations on models in the
    feedback application.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'feedback':  # Ensure feedback models use feedback_db
            return 'feedback_db'
        return None  # Use default for all other apps

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'feedback':
            return 'feedback_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'feedback' or obj2._meta.app_label == 'feedback':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'feedback':
            return db == 'feedback_db'
        return None

# routers.py

class TaskRouter:
    """
    A router to control all database operations on models in the
    feedback application.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Task':  # Ensure feedback models use feedback_db
            return 'task_db'
        return None  # Use default for all other apps

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Task':
            return 'task_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'Task' or obj2._meta.app_label == 'Task':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Task':
            return db == 'task_db'
        return None
