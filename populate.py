from main import Post, User, session

# new_user = User (
#     username = 'testuser',
#     email = 'testuser@test.com'
# )

# session.add(new_user)
# session.commit()

post =[
    {
    "title": "Learn Django",
    "content": "Learn Django in 30 days",
    },
    {
    "title": "Learn JavaScript",
    "content": "Learn JavaScript in 30 days",
    },
    {
    "title": "Learn React",
    "content": "Learn React in 30 days",
    },
    {
    "title": "Learn TypeScript",
    "content": "Learn TypeScript in 30 days",
    },
    {
    "title": "Learn Flask",
    "content": "Learn Flask in 30 days",
    }
]

user = session.query(User).filter(User.id == 1).first()

# for post in post:
#     new_post = Post(
#         title = post['title'],
#         content = post['content'],
#         author = user
#     )

#     session.add(new_post)
#     session.commit()

# print(f"post created {post['title']}")


post = session.query(Post).filter(Post.id == 1).first()
print(post.author)
print (user.post) # second time, we use populate instead of backref so backwards is used on both tables while backward is actually used on one table