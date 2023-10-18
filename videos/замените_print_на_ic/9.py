from icecream import ic

ic.configureOutput(prefix='What it is | ')
ic(1)
ic({"hello": "world"})

ic.configureOutput(prefix='Hello | ')
ic(1)
ic({"hello": "world"})