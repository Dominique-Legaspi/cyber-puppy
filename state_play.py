import puppy_state
import state_asleep

class StatePlay(puppy_state.PuppyState):
    """Returns the events when the Puppy object is in StatePlay"""
    def feed(self, puppy):
        """Puppy object stays in StatePlay"""
        return "The puppy is too busy playing with the ball to eat right now."
    
    def play(self, puppy):
        """Returns a string each time the Puppy object calls the play method, changing state to StateAsleep when number of plays exceeds 3"""
        puppy.inc_plays()
        if puppy.plays < 3:
            return "You throw the ball again and the puppy excitedly chases it."
        else:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            return "You throw the ball again and the puppy excitedly chases it.\nThe puppy played so much it fell asleep!"
            