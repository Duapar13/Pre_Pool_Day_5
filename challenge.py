import random
import time

start_time = time.time()

randomlist = [random.randint(1, 1000000) for _ in range(1000000)]
randomlist.sort()

end_time = time.time()

execution_time = end_time - start_time
print(randomlist)
print(f"Liste triée en {execution_time:.2f} secondes.")
