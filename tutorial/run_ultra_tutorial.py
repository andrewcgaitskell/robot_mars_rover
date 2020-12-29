import ultra
for i in range(10):
  time.sleep(1)
  distance = ultra.checkdist()
  print(distance)
