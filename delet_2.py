from main-oneToOne import Parent, Child, session



parent_to_delete = session.query(Parent).filter(Parent.id == 1).first()
session.delete(parent_to_delete)
session.commit()
# print(parent_to_delete)
# print (parent_to_delete.children)

print(f"Parents {session.query(Parent).all()}")

print(f"Children {session.query(Child).all()}")