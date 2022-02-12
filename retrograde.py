# what am I doing with my time
import numpy as np
from astropy.time import Time
from copy import copy
from planets import Mercury, Venus, Earth, Mars, Jupiter, Saturn

def observed_positions(*Planets, Ref):
    
    Ref.cartesian()
    for Planet in Planets:
        Planet.cartesian()
        Planet.obs_x = Planet.x - Ref.x
        Planet.obs_y = Planet.y - Ref.y
        Planet.obs = np.rad2deg( np.arctan2(Planet.obs_y, Planet.obs_x) ) % 360 # [DEG]
        
    return 0

def retrograde(Planet, Planet_tmr, Planet_ystr):
    
    mv_y = Planet.obs - Planet_ystr.obs
    mv_t = Planet_tmr.obs - Planet.obs
    
    if Planet.obs + 180 < Planet_ystr.obs:
        mv_y += 360
        
    if Planet_tmr.obs + 180 < Planet.obs:
        mv_t += 360
    
    if mv_y < 0 and mv_t < 0:
        Planet.retrograde = True
        print(f'{Planet.name} is in retrograde!')
    else:
        Planet.retrograde = False
        print(f'{Planet.name} is not in retrograde.')
            
    return 0
    

def main():
    
    now = Time.now()
    other = Time('2022-02-07 00:00:00')
    
    t = now
    print(f'Date and time: {t.iso} UTC')
    
    tmr = Time(t.jd + 1, format='jd')
    ystr = Time(t.jd - 1, format='jd')
    
    Mercury.update( tmr ); Mercury_tmr = copy( Mercury )
    Venus.update(   tmr ); Venus_tmr   = copy( Venus   )
    Earth.update(   tmr ); Earth_tmr   = copy( Earth   )
    Mars.update(    tmr ); Mars_tmr    = copy( Mars    )
    Jupiter.update( tmr ); Jupiter_tmr = copy( Jupiter )
    Saturn.update(  tmr ); Saturn_tmr  = copy( Saturn  )
    
    Mercury.update( ystr ); Mercury_ystr = copy( Mercury )
    Venus.update(   ystr ); Venus_ystr   = copy( Venus   )
    Earth.update(   ystr ); Earth_ystr   = copy( Earth   )
    Mars.update(    ystr ); Mars_ystr    = copy( Mars    )
    Jupiter.update( ystr ); Jupiter_ystr = copy( Jupiter )
    Saturn.update(  ystr ); Saturn_ystr  = copy( Saturn  )

    Mercury.update( t )
    Venus.update(   t )
    Earth.update(   t )
    Mars.update(    t )
    Jupiter.update( t )
    Saturn.update(  t )
    
    observed_positions(Mercury,
                       Venus,
                       Mars,
                       Jupiter,
                       Saturn,
                       Ref = Earth)

    observed_positions(Mercury_tmr,
                       Venus_tmr,
                       Mars_tmr,
                       Jupiter_tmr,
                       Saturn_tmr,
                       Ref = Earth_tmr)
    
    observed_positions(Mercury_ystr,
                       Venus_ystr,
                       Mars_ystr,
                       Jupiter_ystr,
                       Saturn_ystr,
                       Ref = Earth_ystr)
    
    retrograde(Mercury,
               Mercury_tmr,
               Mercury_ystr)
    
    retrograde(Venus,
               Venus_tmr,
               Venus_ystr)
    
    retrograde(Mars,
               Mars_tmr,
               Mars_ystr)
    
    retrograde(Jupiter,
               Jupiter_tmr,
               Jupiter_ystr)
    
    retrograde(Saturn,
               Saturn_tmr,
               Saturn_ystr)

    
if __name__ == '__main__':
    main()
