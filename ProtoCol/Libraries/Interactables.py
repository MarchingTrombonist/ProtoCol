"""
A library of interactable elements to add to ProtoCol UI.
"""

from typing import Union, Tuple, Sequence

# Private vars
_next_id = 0
_Interactable_Dict = {}


# Private Classes
class __Interactable:

    def __init__(self, label: str = None):
        """
        Base class for all UI interactables.

        IDs automatically assigned on object creation.

        Parameters
        ----------
        label : str, default None
            Displayed label. None results in label being InteractableType_ID, e.g., "Button_0".
        """
        global _next_id, _Interactable_Dict
        self.__id = _next_id
        if label == None:
            label = f"{type(self).__name__}_{self.__id}"
        self.label = label
        _next_id += 1

        _Interactable_Dict[self.__id] = self
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
    """
    Extends Interactable class.

    Attributes
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
    return _Interactable_Dict.get(id)


def getAll(
    kinds: Union[type, Tuple[type]] = None,
    ids: Union[int, Sequence[int,]] = None,
):
    """
    Return all Interactables with optional conditions.

    Returns *intersection* of all conditions. Default for any unspecified conditions is all items.

    Parameters
    ----------
    kinds : type or tuple of type, default None
        Returns only objects of specified class/es. Default returns all.

    ids: int or sequence of ints, default None
        Returns only objects with IDs in sequence. Default returns all.

    Returns
    -------
    list
        All Interactables as list.
    """
    if kinds == None:
        kinds = __Interactable

    if ids == None:
        ids = range(len(_Interactable_Dict))

    if type(ids) == int:
        ids = (ids,)

    return [
        (k, v)
        for k, v in _Interactable_Dict.items()
        if issubclass(type(v), kinds) and v.getID() in ids
    ]
