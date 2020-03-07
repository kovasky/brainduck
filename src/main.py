from brainduck import BrainDuck

bd = BrainDuck()

bd.parse('example.bf')

for a in bd.tree:
    print(a)
