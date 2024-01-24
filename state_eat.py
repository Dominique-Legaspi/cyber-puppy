import puppy_state
import state_play
import state_asleep

class StateEat(puppy_state.PuppyState):
    """Returns the events when the Puppy object is in StateEat"""
    def feed(self, puppy):
        """Returns a string each time the Puppy object calls the feed method, changing state to StateAsleep when number of feeds exceeds 3"""
        puppy.inc_feeds()
        if puppy.feeds < 3:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
        else:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            return "The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy ate so much it fell asleep!"
    
    def play(self, puppy):
        """Puppy object changes to StatePlay and increments plays"""
        puppy.change_state(state_play.StatePlay())
        puppy.inc_plays()
        return "The puppy looks up from its food and chases the ball you threw."