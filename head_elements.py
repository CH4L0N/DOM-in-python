from element_ABC import Element

class Head(Element):
    """
    Class represents the <head> tag object of the HTML document.
    Only 1 instance of this class should be created per document.
    """
   
    def __repr__(self):
        self._unpack_children()
        return f"<head>\n{str(self._unpacked_children)}\n</head>"


class Meta(Element):
    """
    Class represents the <meta> tag object of the HTML document.
    Only 1 instance of this class should be created per document.
    :param str charset: Encoding of the HTML document (UTF-8 by default).
    """

    def __init__(self, charset="UTF-8"):
        self._charset = charset
    
    def __repr__(self):
        return f"<meta charset=\"{self._charset}\"/>"
    

class Title(Element):
    """
    Class represents the <title> tag object of the HTML document.
    Only 1 instance of this class should be created per document.
    :param str text: Content of the <title> tag.
    """
    def __init__(self, text):
        self._text = text
    
    def __str__(self):
        return f"<title>{self._text}</title>"