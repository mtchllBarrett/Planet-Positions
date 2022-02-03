# defines the Planet object and sets all the important data for each planet

# this data was taken from a text file
# I wanted to just load it all in using np.loadtxt, but it didn't behave nicely...
# ...so I painstakingly put all these values in manually like a crazy person

from functions import Newton, Kepler, get_f, get_l, get_r
from quantities import J2000, Cy

class Planet:
    
    def __init__(self, name, a,e,I,L,ap,ln,da,de,dI,dL,dap,dln):
        
        self.name = name
        
        self.a_J2000 = a # semimajor axis                            [AU]
        self.e_J2000 = e # eccentricity
        self.I_J2000 = I # inclination                               [deg]
        self.L_J2000 = L # mean longitude                            [deg]
        self.arg_peri_J2000 = ap # argument of periapsis             [deg]
        self.long_node_J2000 = ln # longitude of the ascending node  [deg]
        
        # changes in the above quantities, in units of [quantity] / century
        self.delta_a = da
        self.delta_e = de
        self.delta_I = dI
        self.delta_L = dL
        self.delta_arg_peri = dap
        self.delta_long_node = dln
        
        self.long_peri_J2000 = self.arg_peri_J2000 + self.long_node_J2000
        self.delta_long_peri = self.delta_arg_peri + self.delta_long_node
        
    def update(self, t):
        dt = (t.jd - J2000) / Cy
        # gets current values for parameters given some timestep dt
        self.a = self.a_J2000 + self.delta_a * dt
        self.e = self.e_J2000 + self.delta_e * dt
        self.I = self.I_J2000 + self.delta_I * dt
        self.L = self.L_J2000 + self.delta_L * dt 
        self.arg_peri = self.arg_peri_J2000 + self.delta_long_peri * dt
        self.long_node = self.long_node_J2000 + self.delta_long_node * dt
        self.long_peri = self.long_peri_J2000 + self.delta_long_peri * dt
        
        self.L %= 360 # since L just goes around forever, move it back to the interval [0, 360)
        
        self.M = self.L - self.long_peri # mean anomaly
        
        # solve for the eccentric anomaly using Newton's method:
        self.E = Newton(
                        self.M, # M is a reasonable initial guess for E to start Newton's method
                        lambda x : Kepler(x, self.e, self.M),
                        lambda x : Kepler(x, self.e, self.M, deriv=True)
                       )
        
        self.f = get_f(self.E, self.e)              # true anomaly      [DEG]
        self.l = get_l(self.f, self.long_peri)      # true longitude    [DEG]
        self.r = get_r(self.a, self.e, self.E)      # distance from sun [AU]

Mercury = Planet('Mercury',
                 0.38709927,
                 0.20563593,
                 7.00497902,
               252.25032350,
                77.45779628,
                48.33076593,
                 0.00000037,
                 0.00001906,
                -0.00594749,
            149472.67411175,
                 0.16047689,
                -0.12534081)

Venus = Planet('Venus',
               0.72333566,
               0.00677672,
               3.39467605,
             181.97909950,
             131.60246718,
              76.67984255,
               0.00000390,
              -0.00004107,
              -0.00078890,
           58517.81538729,
               0.00268329,
              -0.27769418)

Earth = Planet('Earth',
               1.00000261,
               0.01671123,
              -0.00001531,
             100.46457166,
             102.93768193,
               0.00000000,
               0.00000562,
              -0.00004392,
              -0.01294668,
           35999.37244981,
               0.32327364,
               0.00000000)

Mars = Planet('Mars',
              1.52371034,
              0.09339410,
              1.84969142,
             -4.55343205,
            -23.94362959,
             49.55953891,
              0.00001847,
              0.00007882,
             -0.00813131,
          19140.30268499,
              0.44441088,
             -0.29257343)

Jupiter = Planet('Jupiter',
                 5.20288700,
                 0.04838624,
                 1.30439695,
                34.39644051,
                14.72847983,
               100.47390909,
                -0.00011607,
                -0.00013253,
                -0.00183714,
              3034.74612775,
                 0.21252668,
                 0.20469106)

Saturn = Planet('Saturn',
                9.53667594,
                0.05386179,
                2.48599187,
               49.95424423,
               92.59887831,
              113.66242448,
               -0.00125060,
               -0.00050991,
                0.00193609,
             1222.49362201,
               -0.41897216,
               -0.28867794)

Uranus = Planet('Uranus',
               19.18916464,
                0.04725744,
                0.77263783,
              313.23810451,
              170.95427630,
               74.01692503,
               -0.00196176,
               -0.00004397,
               -0.00242939,
              428.48202785,
                0.40805281,
                0.04240589)

Neptune = Planet('Neptune',
                30.06992276,
                 0.00859048,
                 1.77004347,
               -55.12002969,
                44.96476227,
               131.78422574,
                 0.00026291,
                 0.00005105,
                 0.00035372,
               218.45945325,
                -0.32241464,
                -0.00508664)