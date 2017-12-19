from apppy import app , db
from flask.ext.script import Manager , prompt_bool

mgr = Manager(app)

@mgr.command
def init_db():
    db.create_all()
    print "Initialized database"

@mgr.command
def drop_db():
    if prompt_bool("Are u sure ?"):
        db.drop_all()
        print "Database dropped!"

if __name__ == "__main__":
    mgr.run()
