def format_float(number):
    return float(format(number, '.2f'))

def calc_years(seconds, orb_period = 1):
    period = 365.25 * orb_period
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days/period
    return years

class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return format_float(calc_years(self.seconds))
    def on_mercury(self):
        return format_float(calc_years(self.seconds, 0.2408467))
    def on_venus(self):
        return format_float(calc_years(self.seconds, 0.61519726))
    def on_mars(self):
        return format_float(calc_years(self.seconds, 1.8808158))
    def on_jupiter(self):
        return format_float(calc_years(self.seconds, 11.862615))
    def on_saturn(self):
        return format_float(calc_years(self.seconds, 29.447498))
    def on_uranus(self):
        return format_float(calc_years(self.seconds, 84.016846))
    def on_neptune(self):
        return format_float(calc_years(self.seconds, 164.79132))
