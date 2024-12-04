m = MTransformationMatrix()
m.setTranslation(MVector(2, 3, 4), om.MSpace.kWorld)
m.setRotation(om.MEulerRotation(0, 20, 0))
m.setScale(MVector(2.5, 3.12, 4.2), om.MSpace.kWorld)
print(m.asMatrix())

# extract the data

print(m.rotation())
print(m.scale(om.MSpace.kWorld))
print(m.translation(om.MSpace.kWorld))
