from main import User, Session, engine

local_session = Session(bind=engine)
#return all objects in the database
# users = local_session.query(User).all()[:3]

# query for one object

jana = local_session.query(User).filter(User.username=='Jana').first()      # first() returns the first object in the query, in case of multiple objects
print(jana)
# for user in users:
#     print(user.username)