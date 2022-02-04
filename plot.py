import numpy as np
import matplotlib.pyplot as plt
from functions import rad

def mkfig(time_string, *Planets, sketch_orbit = True):
    # this should be passed planet objects
    
    # initialize some variables for the function
    figsize = (6,6)
    size = 1
    dpi = 150
    saveas = 'solarsystem'
    outermost = ''
    time_fmt = time_string.replace(' ', '_').replace(':', '-')
    
    planet_ls = ''
    planet_marker = 'o'
    
    if sketch_orbit:
        num_pts = 1000
        theta_range = np.linspace(0, 2*np.pi, num = num_pts)
        orbit_ls = '--'
        orbit_marker = ''
        
    
    # plot things
    fig, ax = plt.subplots(figsize = figsize)
    
    # plot the sun
    ax.plot(0, 0,
            linestyle = planet_ls,
            marker = '*',
            color = 'yellow')
    
    for Planet in Planets:
        
        Planet.x = Planet.r * np.cos( rad( Planet.l ))
        Planet.y = Planet.r * np.sin( rad( Planet.l ))
        
        if Planet.a > size:
            size = Planet.a * 1.1
            outermost = Planet.name.lower()
            
        ax.plot(Planet.x, 
                Planet.y,
                linestyle = planet_ls,
                marker = planet_marker,
                label = Planet.name,
                color = Planet.hexcolor)
        
        if sketch_orbit:
            
            orbit_xvals = Planet.a * np.cos(theta_range)
            orbit_yvals = Planet.a * np.sin(theta_range)
            
            ax.plot(orbit_xvals,
                    orbit_yvals,
                    linestyle = orbit_ls,
                    marker = orbit_marker,
                    color = Planet.hexcolor)
    
    ax.set_xlim(-size, size)
    ax.set_ylim(-size, size)
    
    # ax.legend()
    
    ax.set_title(f'Planet orbital positions on {time_string}')
    ax.set_xlabel('Distance from sun [AU]')
    ax.set_ylabel('Distance from sun [AU]')
    
    fig.savefig(f'{saveas}_{outermost}_{time_fmt}', dpi=dpi)