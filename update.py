from main_db import User, Session, engine

local_session = Session(bind=engine)

user_to_update = local_session.query(User).filter(User.username=='Jana').first()

user_to_update.username = 'Janaswain'
user_to_update.email = 'janaswain@company.com'

local_session.commit()