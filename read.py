from main import User, Session, engine
localsession = Session(bind=engine)

user_to_read = localsession.query (User).all()
print(user_to_read)
