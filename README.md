# Planet-Positions

At some point, I'm sure this will be a more interesting program.
For now, it just does some math.

For some date and time, this will calculate the positions of all the planets around the sun.
The data values in `planets.py` are supposedly valid between years 1800 and 2050.

On running, generates two plots: one extending to Mars' orbit, and one extending to Neptune's orbit.
The plots include dashed-line circles to show orbits, except orbits are actually ellipses so it's slightly inaccurate.
Eventually it would be ideal to plot the correct ellipses, although mathematically circles are so much easier.

`retrograde.py` will tell you if any planets are currently in retrograde. 
If you would like to know about a different day, set the `other` time object to the ISO UTC date you want to know about
and change the line `t = now` to `t = other`. 
