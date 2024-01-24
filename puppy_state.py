import abc
class PuppyState(abc.ABC):
    """Abstract interface that passes the feed and play methods"""
    @abc.abstractmethod
    def feed(self, puppy):
        pass
    
    @abc.abstractmethod
    def play(self, puppy):
        pass