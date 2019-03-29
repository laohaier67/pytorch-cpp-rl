"""
Classes for building requests to send to pytorch-cpp-rl.
"""
from abc import ABC, abstractmethod
import numpy as np
import msgpack


class Message(ABC):
    """
    Base class for messages.
    """
    @abstractmethod
    def to_msg(self) -> bytes:
        """
        Creates the JSON for the request.
        """
        pass


class MakeMessage(Message):
    """
    Builds the JSON for returning the result of an make_env() action.
    """

    def to_msg(self) -> bytes:
        request = {
            "result": "OK"
        }
        return msgpack.packb(request)


class ResetMessage(Message):
    """
    Builds the JSON for returning the result of an env.reset() action.
    """

    def __init__(self, observation: np.ndarray):
        self.observation = observation

    def to_msg(self) -> bytes:
        request = {
            "observation": self.observation.tolist()
        }
        return msgpack.packb(request)


class StepMessage(Message):
    """
    Builds the JSON for returning the result of an env.step() action.
    """

    def __init__(self,
                 observation: np.ndarray,
                 reward: np.ndarray,
                 done: np.ndarray):
        self.observation = observation
        self.reward = reward
        self.done = done

    def to_msg(self) -> bytes:
        request = {
            "observation": self.observation.tolist(),
            "reward": self.reward.tolist(),
            "done": self.done.tolist()
        }
        return msgpack.packb(request)