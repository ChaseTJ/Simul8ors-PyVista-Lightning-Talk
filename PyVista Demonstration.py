'''
Simul8ors PyVista Demonstration for ME 396 Lightning Talk
Goes over some of the features of the PyVista Library
-Ang Gao- -Chase Johnson- -Leo Kern-
'''

import pyvista as pv
import numpy as np

# %% Basic Mesh Plotting Example

# groot_big = pv.read('Waving_Groot_15.5cm.stl')
# groot = groot_big.decimate(0.9)
# groot.save('groot.stl')

groot = pv.read('groot.stl')

# Creating the plotter
p = pv.Plotter()

# Adding the cow mesh to the plotter, setting the color to burn orange and turning on smooth shading
p.add_mesh(groot, color='#CC5500', smooth_shading=False, show_edges=False)

p.camera_position = [
    [0, -300, 100],   # Position: Camera location in space
    [75, 100, 75],   # Focal point: Point where the camera is looking (the center of the sphere)
    [0, 0, 1]    # View up: The "up" direction in the camera's view
]

p.show()


# %% Plane Widget Example
# https://tutorial.pyvista.org/tutorial/08_widgets/e_plane-widget.html

# vol = pv.examples.download_brain()

# p = pv.Plotter()
# p.add_mesh_slice(vol)
# p.show()

# %% Sphere Widget Example
# https://tutorial.pyvista.org/tutorial/08_widgets/g_sphere-widget.html


# from scipy.interpolate import griddata


# def get_colors(n):
#     """A helper function to get n colors."""
#     from itertools import cycle

#     import matplotlib as mpl

#     cycler = mpl.rcParams["axes.prop_cycle"]
#     colors = cycle(cycler)
#     return [next(colors)["color"] for i in range(n)]


# # Create a grid to interpolate to
# xmin, xmax, ymin, ymax = 0, 100, 0, 100
# x = np.linspace(xmin, xmax, num=25)
# y = np.linspace(ymin, ymax, num=25)
# xx, yy, zz = np.meshgrid(x, y, [0])

# # Make sure boundary conditions exist
# boundaries = np.array([[xmin, ymin, 0], [xmin, ymax, 0], [xmax, ymin, 0], [xmax, ymax, 0]])

# # Create the PyVista mesh to hold this grid
# surf = pv.StructuredGrid(xx, yy, zz)

# # Create some initial perturbations
# # - this array will be updated inplace
# points = np.array([[33, 25, 45], [70, 80, 13], [51, 57, 10], [25, 69, 20]])


# # Create an interpolation function to update that surface mesh
# def update_surface(point, i) -> None:
#     points[i] = point
#     tp = np.vstack((points, boundaries))
#     zz = griddata(tp[:, 0:2], tp[:, 2], (xx[:, :, 0], yy[:, :, 0]), method="cubic")
#     surf.points[:, -1] = zz.ravel(order="F")


# # Get a list of unique colors for each widget
# colors = get_colors(len(points))
# # Begin the plotting routine
# p = pv.Plotter()

# # Add the surface to the scene
# p.add_mesh(surf, color=True)

# # Add the widgets which will update the surface
# p.add_sphere_widget(update_surface, center=points, color=colors, radius=3)
# # Add axes grid
# p.show_grid()

# # Show it!
# p.show()

# %% Filters example
# https://tutorial.pyvista.org/tutorial/04_filters/bonus/f_sampling_functions_3d.html#sphx-glr-tutorial-04-filters-bonus-f-sampling-functions-3d-py

# freq = (1, 1, 1)
# noise = pv.perlin_noise(1, freq, (0, 0, 0))
# grid = pv.sample_function(noise, [0, 3.0, -0, 3.0, 0, 3.0], dim=(120, 120, 120))
# out = grid.threshold(0.02)
# out
# mn, mx = [out["scalars"].min(), out["scalars"].max()]
# clim = (mn, mx * 1.8)

# p = pv.Plotter()

# out.add_mesh(
#     cmap="gist_earth_r",
#     background="white",
#     show_scalar_bar=False,
#     lighting=True,
#     clim=clim,
#     show_edges=False,
# )

# p.add_mesh_threshold(out)

# p.show()