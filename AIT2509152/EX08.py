mewhenI = '{} {} {} {}'

print(mewhenI.format(1,2,3,4))
print(mewhenI.format("one","two","three","four"))
print(mewhenI.format(bool(1),bool(0),f"{float(True):.3f}",int(False)))
print(mewhenI.format(mewhenI,mewhenI,mewhenI,mewhenI))
print(mewhenI.format(
    'Me',
    'when',
    'I',
    'explode'
    )
)