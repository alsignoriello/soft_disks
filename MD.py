#!/usr/bin/python
from velocity_verlet import *
import numpy as np
from parser import write_coords
from plot import plot_voronoi, plot_disks


"""

MD.py - molecular dynamics simulation for disks
author: Lexi Signoriello
date: 4/5/16

plot to disks folder every 100 time steps


"""

def molecular_dynamics(particles, dt, Nt, parameters):

	# store kinetic energy for every time step
	E_k = np.zeros(Nt)

	# store potential energy for every time step
	E_p = np.zeros(Nt)

	# spring potential
	k = parameters['k']

	# length of box
	lx = parameters['Lx']
	ly = parameters['Ly']
	L = np.array([lx,ly])

	# drag coefficient
	B = parameters['B']

 
	for t in range(0,Nt):

		# Integrate Newton's Equations of Motion
		# using velocity verlet algorithm

		# (x,y) += dt * v(t) + 1/2 * a(t) * dt^2
		get_positions(particles, dt, L)


		# calculate forces for particle-particle interactions
		ep, forces, accels = get_forces(particles, k, L, B)
		E_p[t] = ep


		# calculate new velocities
		# v(t+1) = v(t) + 1/2(a(t) + a(t+1)) * dt
		ek = get_velocities(particles, accels, dt)
		E_k[t] = ek

		# write coordinates to file every 100 time steps
		if t % 100 == 0 and t > 500:
			print t
			write_coords(particles, t)
			plot_voronoi(particles, L, "k", t)
			plot_disks(particles, L, "c", False, t)


	np.savetxt("kinetic_energy.txt", E_k)
	np.savetxt("potential_energy.txt", E_p)











		