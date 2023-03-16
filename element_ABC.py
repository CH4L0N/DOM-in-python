from abc import ABC

class Element(ABC):
    """
    Class represents the general element to be added into the <body> tag object.
    This is an abstract base class intended only for inheritance purposes.
    No instances of this class should ever be created.
    """

    def __init__(self, id="", classname=""):
        self._id = id
        self._classname = classname
        self._children = []
    

    def _unpack_children(self):
        """
        Unpacks the children elements contained in the self._children list.
        """
        self._unpacked_children = "\n".join(str(_) for _ in self._children)


    def set_attribute(self, attribute, value):
        """
        Sets the element's attribute to given value.
        :param str attribute: Either 'id' or 'class'.
        :param str value: Value to be set as attribute.
        :raises ValueError: Enter either 'id' or 'class' as parameter.
        """
        try:
            if attribute == "id":
                self._id = value
            elif attribute == "class":
                self._classname = value
        except:
            raise ValueError("Enter either 'id' or 'class' as parameter.")
    

    def get_attribute(self, attribute):
        """
        Returns the element's attribute based on attribute specified in the parameter.
        :param str attribute: Either 'id' or 'class'.
        :raises ValueError: Enter either 'id' or 'class' as parameter.
        """
        try:
            if attribute == "id":
                return self._id
            elif attribute == "class":
                return self._classname
        except:
            raise ValueError("Enter either 'id' or 'class' as parameter.")


    def add_child(self, child):
        """
        Checks whether child to be added is an instance of Element and appends it to the list of children if true.
        :param Element child: Another tag object to be added as a child. Must be of Element object type.
        :raises TypeError: Child must be an instance of Element.
        """
        try:
            if isinstance(child, Element):
                self._children.append(child)
        except:
            raise TypeError("Child must be an instance of Element.")


    def remove_child(self, child):
        """
        Checks whether child to be removed is contained within the ancestor's children list and removes it if true.
        :param Element child: Another tag object to be removed as a child.
        :raises ValueError: Child was not found.
        """
        try:
            if child in self._children:
                self._children.remove(child)
        except:
            raise ValueError("Child was not found.")