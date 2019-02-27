import numpy as np
from stl import mesh
from tqdm import tqdm
import matplotlib.pyplot as plt

stl_mesh = mesh.Mesh.from_file('./stl/Body.stl')
areas = []
zs = []
for triangle in tqdm(stl_mesh.vectors):
    a = triangle[0]-triangle[1]
    b = triangle[0]-triangle[2]
    n = np.cross(a, b)
    area = np.sqrt(n.dot(n))/2
    areas.append(area)
    z = triangle[:, 2].mean()
    zs.append(z)
areas = np.array(areas)
zs = np.array(zs)
new_vectors = stl_mesh.vectors[np.where((areas < 200) | (zs > 75) | (zs < -125)), :, :]
data = np.zeros(new_vectors.shape[1], dtype=mesh.Mesh.dtype)
data['vectors'] = new_vectors
new_mesh = mesh.Mesh(data.copy())
new_mesh.save('./new_stl_file.stl')
