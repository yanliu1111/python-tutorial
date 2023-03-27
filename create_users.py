from main_db import User, Session, engine

users = [{
"username": "Tom",
"email": "tom@test.com"
},{"username": "Jerry",
"email": "jerry@test.com"
},{"username": "Lily",
"email": "lily@test.com"
},{"username": "Jack",
"email": "jack@test.com"
},{"username": "Tom",
"email": "Fred@test.com"
},{"username": "Tom",
"email": "fred@test.com"
},]

local_session = Session(bind=engine)

# new_user = User(username='Jana',email='jana@company.com')
# local_session.add(new_user)
# local_session.commit() 

for u in users:
    new_user = User(username=u['username'],email=u['email'])
    # print (new_user)
    local_session.add(new_user)
    local_session.commit() # add to the database
    print(f"Added user {u['username']}")
       