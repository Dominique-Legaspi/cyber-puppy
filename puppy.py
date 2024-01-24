import state_asleep
class Puppy:
    """Puppy object that the user interacts with
    
    Attributes:
        _state: represents the state of the Puppy object
        _feeds: integer representing the number of feeds
        _plays: integer representing the number of plays
    """
    def __init__(self):
        """Initializes the Puppy object in the Asleep state"""
        self._state = state_asleep.StateAsleep()
        self._feeds = 0
        self._plays = 0
        
    @property
    def feeds(self):
        return self._feeds
        
    @property
    def plays(self):
        return self._plays
        
    def change_state(self, new_state):
        """Changes the state of the Puppy object"""
        self._state = new_state
        
    def throw_ball(self):
        """Returns the play method"""
        return self._state.play(self)
    
    def give_food(self):
        """Returns the feed method"""
        return self._state.feed(self)
    
    def inc_feeds(self):
        """Increases the number of feeds by 1"""
        self._feeds += 1
        
    def inc_plays(self):
        """Increases the number of plays by 1"""
        self._plays += 1
    
    def reset(self):
        """Resets the number of feeds and plays to 0"""
        self._feeds = 0
        self._plays = 0