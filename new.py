# Just learning git/github!
# And python. And data structures and algorithms!
# And a lot of things actually.

import os
import sys
import time

pid = os.fork()

if (pid==0):
	print(f"[Child {os.getpid()}] Doing something hard...")

	time.sleep(5)
	sys.exit(0)

else:
	print(f"[Parent {os.getpid()}] Waiting for child.")

	os.wait()
	print(f"[Parent {os.getpid()}] Completed! Exiting.")


print("done.")
print("exit")
