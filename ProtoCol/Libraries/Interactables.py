"""
A library of interactable elements to add to ProtoCol UI.
"""

from collections import namedtuple

# Private vars
_next_id = 0
_Interactable_Dict = {}
_Interactable_Dict_Simple = {}


# Private Classes
class __Interactable:

    def __init__(self, label: str = None):
        """
        Base class for all UI interactables.

        IDs automatically assigned on object creation.

        Parameters
        ----------
        label : str, default None
            Displayed label.
        """
        global _next_id, _Interactable_Dict, _Interactable_Dict_Simple
        self.__id = _next_id
        self.label = label
        _next_id += 1

        # Appends a namedtuple to the dict list of all interactables
        _Interactable_Dict[self.__id] = namedtuple(
            type(self).__name__, ["id", "type", "object"]
        )(id=self.__id, type=type(self).__name__, object=self)

        _Interactable_Dict_Simple[self.__id] = self
        return

    def getID(self):
        """
        Return ID of object.

        Returns
        -------
        int
            ID of object.
        """
        return self.__id

    # TODO: unneeded? no reason for label to be private probably
    def getLabel(self):
        """
        Return label of Interactable.

        Returns
        -------
        str
            Label of Interactable.
        """
        return self.label

    def toString(self, debug: bool = False, as_dict: bool = False):
        """
        Return all attributes of this Interactable as a string.

        Returns class variables only.

        Parameters
        ----------
        debug : bool, default False
            Currently unimplemented. If True, returns extra information.
        as_dict : bool, default False
            If True, returns as dict instead of str.

        Returns
        -------
        str
            Attributes as string
        """
        # removes special attributes
        attribute_list = [a for a in dir(self) if not a.startswith("__")]
        # separates variables and functions
        var_list = [v for v in attribute_list if not callable(getattr(self, v))]
        var_dict = {k: getattr(self, k) for k in var_list}

        # TODO; return function names on debug?
        # func_list = [f for f in attribute_list if callable(getattr(self, f))]
        # func_dict = {k: str(getattr(modules, k)) for k in func_list}

        if as_dict:
            return var_dict

        output = (
            f"ToString unspecified - This {type(self).__name__} has values: {var_dict}"
        )

        return output


# Public Classes
class Button(__Interactable):
    def __init__(self, action=lambda: print("Click!"), *args, **kwargs):
        """
        Create a button.

        Extends Interactable class.

        Parameters
        ----------
        label : str, default None
            Displayed label.

        action : function, default print("Click!")
            Function to be called on trigger.

        args : any
            These parameters will be passed to the provided function.

        kwargs : any
            These parameters will be passed to the provided function.
        """
        super().__init__()
        self.__action = action
        self.__args = args
        self.__kwargs = kwargs
        return

    def trigger(self):
        """
        Call provided function.
        """
        try:
            self.__action(*self.__args, **self.__kwargs)
        except TypeError as e:
            print(f"TypeError: {e}")
            print("Double check your arguments")
            print("Continuing Execution")
        except Exception as e:
            print(e)
        return


class Toggle(__Interactable):

    def __init__(self, state: bool = False):
        """
        TODO.

        Extends Interactable class

        Parameters
        ----------
        label : str, default None
            Displayed label.


        """
        super().__init__()
        self.__state = state
        return

    def toggle(self):
        """
        TODO
        """
        self.__state = not self.__state
        return


class Slider(__Interactable):

    def __init__(self, low: int = 0, high: int = 100, value: int = 50):
        """
        TODO.

        Extends Interactable class.

        Parameters
        ----------
        label : str, default None
            Displayed label.
        """
        super().__init__()
        self.low = low
        self.high = high
        self.value = value
        return

    def set_value(self, new_value: int):
        """
        TODO
        """
        if self.low <= new_value <= self.high:
            self.state = new_value
        else:
            raise Exception(
                f"Value {new_value} out of range for slider with range [{self.low}, {self.high}]"
            )
        return


# Module Functions
def getByID(id: int, debug: bool = False):
    """
    TODO
    """
    if debug:
        return _Interactable_Dict.get(id)
    return _Interactable_Dict.get(id).object


def getAll(debug: bool = False):
    """
    Return all Interactables.

    Parameters
    ----------
    debug : bool, default False
        If True, returns dict with more info.

    Returns
    -------
    dict
        All Interactables as dict.
    """
    if debug:
        return _Interactable_Dict
    return _Interactable_Dict_Simple
