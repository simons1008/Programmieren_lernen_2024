# Change grid interval and specify tick labels
# Source - https://stackoverflow.com/a/24953575
# Posted by MaxNoe, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-28, License - CC BY-SA 4.0

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Major ticks every 10, minor ticks every 2
major_ticks = np.arange(0, 101, 10)
minor_ticks = np.arange(0, 101, 2)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# And a corresponding grid
ax.grid(which='both')

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

# Title
plt.title("Demo")

# Labels
plt.xlabel("x")
plt.ylabel("y")

plt.show()
