from ProtoCol.Libraries.Interactables import (
    Button,
    getByID,
    Toggle,
    Slider,
    getAll,
)

# debug importing of private vars
import ProtoCol.Libraries.Interactables as intbl


def b_func(id):
    print(getByID(id))


b = Button(b_func, id=1)
t = Toggle()
s = Slider()
items = [b, t, s]
# b.trigger()
# b.toString()

# for i in items:
#     print(i.toString())
#     print(i.getID())

# for i in range(3):
#     print(getByID(i))

# print(getAll())
# for k, v in getAll().items():
#     print(k, v)

# for k, v in intbl._Interactable_Dict.items():
#     print(k, v)
# for k, v in intbl._Interactable_Dict_Simple.items():
#     print(k, v)

# print(getAll(True).values())
print(getAll((Button, Slider)))
print(getAll(Toggle))
print(getAll(ids=0))
print(getAll(ids=(0, 1)))
print(getAll(ids=[0, 1]))
print(getAll(kinds=Toggle, ids=range(2)))
# print([(k, type(v)) for k, v in intbl._Interactable_Dict.items()])
