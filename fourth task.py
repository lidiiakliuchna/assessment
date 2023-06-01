import abc

class Planet(object):
    __metaclass__ = abc.ABCMeta


    @abc.abstractmethod
    def get_distance_to_earth(self, input):
        return

class Sun(Planet):
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type
    def get_distance_to_earth(self):
        distance = round(self.distance_from_sun,2)
        print("distance to earth:", distance)
        return distance


class Mercury(Planet):
   def __init__(self, name, distance_from_sun, planet_type):
      self.name = name
      self.distance_from_sun = distance_from_sun
      self.planet_type = planet_type

   def get_distance_to_earth(self):
      distance = round(self.distance_from_sun, 2)
      print("distance to earth:", distance)
      return distance

print(Sun('Sun',147000000,'Star').get_distance_to_earth())
