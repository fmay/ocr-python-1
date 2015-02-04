
li = list(range(0, 10))

def over_five(elem):
  return elem > 5

# this takes all xs that fit the criteria specified in a function.
filtered_li = [x for x in li if over_five(x)]

print(filtered_li)
