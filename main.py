from astropy.time import Time
from planets import Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

def main():

    t_str = '2022-02-01 18:50:00'   # t_str is the time of interest as an ISO date, 
                                    # entered as a string. The time zone is UTC.
                                    # Ideally this would set via input from the 
                                    # user somehow. Perhaps there could also be a
                                    # way to change the time zone, so that you don't
                                    # necessarily have to enter the time as UTC
                                    # (although I think there's a computerphile
                                    # video of Tom Scott warning people not to 
                                    # attempt such a thing).
    
    t = Time(t_str)             # t_str as an Time object
    
    Mercury.update(t)
    Venus.update(t)
    Earth.update(t)
    Mars.update(t)
    Jupiter.update(t)
    Saturn.update(t)
    Uranus.update(t)
    Neptune.update(t)

    return 0

if __name__ == '__main__':
    main()