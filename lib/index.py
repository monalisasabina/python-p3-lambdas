def myfunc(x):
  return lambda n : n + x

new_century = myfunc(100)

print(new_century(2000))

# => 2100


l = [['red','truck'],['blue','truck'],['red','sedan']]
l1 = sorted(l, key=lambda v: v[1])
# => [['red', 'sedan'], ['red', 'truck'], ['blue', 'truck']]
l2 = sorted(l, key=lambda v: v[1], reverse=True)
# => [['red', 'truck'], ['blue', 'truck'], ['red', 'sedan']]

print(l1)
print(l2)


def myfunc(x):
  return lambda a, b : (a + b) * x

sum_times_2 = myfunc(2)

print(sum_times_2(10, 20))

# => 60
