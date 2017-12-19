from apppy import app , db
from flask.ext.script import Manager , prompt_bool
from apppy.models import User

mgr = Manager(app)

@mgr.command
def init_db():
    db.create_all()
    db.session.add(User(username="Erik",email="erik@gmail.com"))
    db.session.add(User(username="Pacho",email="pacho@gmail.com"))
    db.session.commit()
    print "Initialized database"

@mgr.command
def drop_db():
    if prompt_bool("Are u sure ?"):
        db.drop_all()
        print "Database dropped!"

if __name__ == "__main__":
    mgr.run()
