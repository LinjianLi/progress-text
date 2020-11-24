import random
import time
from progress_text import ProgressText

for i in ProgressText([1, 3, 5, 7, 9, 11, 13]):
    time.sleep(1 + random.random()) # Sleep for [1, 2) seconds.
    pass

for i in ProgressText(range(50), task_name="foo bar"):
    pass

for i in ProgressText(range(10**3), every_percent=20):
    if i % 10**2 == 0:
        time.sleep(10 + 2 * (random.random() - 0.5)) # Sleep for [9, 11) seconds.
    else:
        pass
