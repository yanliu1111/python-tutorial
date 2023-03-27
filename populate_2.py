# one to one relationship
from main-oneToOne import Parent, Child, session

# parent1 = Parent (name = 'Parent 1')
# parent2 = Parent (name = 'Parent 2')

# session.add_all ([parent1, parent2])

# session.commit()

parent1 = session.query(Parent).filter(Parent.id == 1).first()

# child1 = Child (name = 'Child 1', parent = parent1)
# session . add (child1)
# session . commit ()

child2 = Child (name = 'Child 2', parent = parent1)
session . add (child2)
session . commit ()
# childer will be only one object to parent1

print(parent1.children)
