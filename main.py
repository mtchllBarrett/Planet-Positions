from astropy.time import Time
from planets import Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
from plot import mkfig

def main():
    
    t_str = '2022-08-05 18:50:00'   # t_str is the time of interest as an ISO date, 
                                    # entered as a string. The time zone is UTC.
                                    # Ideally this would set via input from the 
                                    # user somehow. Perhaps there could also be a
                                    # way to change the time zone, so that you don't
                                    # necessarily have to enter the time as UTC
                                    # (although I think there's a computerphile
                                    # video of Tom Scott warning people not to 
                                    # attempt such a thing).
    
    make_plots = True               # if you want to make a plot, set to True
                                    # turn off to lower runtime for testing

    t = Time(t_str)                 # t_str (or now) as an Time object
    
    now = Time.now()                # current time; in case you don't have a specific
                                    # time in mind, you can use this instead
    
    time_to_use = now
    
    Mercury.update(time_to_use)
    Venus.update(time_to_use)
    Earth.update(time_to_use)
    Mars.update(time_to_use)
    Jupiter.update(time_to_use)
    Saturn.update(time_to_use)
    Uranus.update(time_to_use)
    Neptune.update(time_to_use)
    
    if make_plots:
        
        mkfig(t_str,
              
              Mercury,
              Venus,
              Earth,
              Mars,
              Jupiter,
              Saturn,
              Uranus,
              Neptune)
        
        # it's hard to see inner planets from Neptune, so I include a second plot
        mkfig(t_str,
              
              Mercury,
              Venus,
              Earth,
              Mars)
    
    return 0

if __name__ == '__main__':
    main()