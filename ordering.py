from main import Session, User, engine

local_session = Session(bind=engine)

#ascending order
users = local_session.query(User).order_by(User.username).all()
for user in users:
    print(f'User {user.username}')

#descending order
users = local_session.query(User).order_by(User.username.desc()).all()
for user in users:
    print(f'De User {user.username}')