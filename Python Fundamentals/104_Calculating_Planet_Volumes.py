

import numpy as np

radii = np.array([2439.7, 6051.8, 6371, 3389.7, 69911, 58232, 25362, 24622])

r = 10
volume = 4/3 * np.pi * r**3
print(volume)

volumes = 4/3 * np.pi * radii**3
print(volumes)


radii = np.random.randint(1, 1000, 1000000)
volumes = 4/3 * np.pi * radii**3
print(volumes)

