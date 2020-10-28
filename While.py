while--
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
----
i = 1
while i < 6:
  print(i)
  if i == 4:
    break
  i += 1