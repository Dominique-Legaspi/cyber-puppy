import puppy_state
import state_eat

class StateAsleep(puppy_state.PuppyState):
    """Returns the events when the Puppy object is in StateAsleep"""
    def feed(self, puppy):
        """Puppy object changes to StateEat and increments feeds"""
        puppy.change_state(state_eat.StateEat())
        puppy.inc_feeds()
        return "The puppy wakes up and comes running to eat."
    
    def play(self, puppy):
        """Puppy object stays in StateAsleep"""
        return "The puppy is asleep. It doesn't want to play right now."