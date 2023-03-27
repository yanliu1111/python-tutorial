from main_db import Base, User, engine

Base.metadata.create_all(engine)
