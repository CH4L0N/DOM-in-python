from element_ABC import Element

class Body(Element):
    """
    Class represents the <body> tag object of the HTML document.
    Only 1 instance of this class should be created per document.
    """
   
    def __repr__(self):
        self._unpack_children()
        return f"<body>\n{str(self._unpacked_children)}\n</body>"


class Input(Element):
    """
    Class represents the <input> tag object of the HTML document.
    Multiple instances of this class may be created in document.
    :param str type: Specifies the element's display type. Values: text, password, submit etc.
    :param str value: Value to be sent to the server.
    :param str placeholder: Specifies the element's text to be shown prior to any user input.
    :param str id: Element's id, must be unique per document. Default: Empty string.
    :param str classname: Element's class, does not need to be unique per document. Default: Empty string.
    """
    
    def __init__(self, type, value, placeholder="", id="", classname=""):
        super().__init__(id, classname)
        self._type = type
        self._value = value
        self._placeholder = placeholder

    def __repr__(self):
        return (
            f'<input id="{self._id}" class="{self._classname}" type="{self._type}" value="{self._value}" placeholder="{self._placeholder}" />'
        )

class Select(Element):
    """
    Class represents the <select> tag object of the HTML document.
    Multiple instances of this class may be created in document.
    :param str id: Element's id, must be unique per document. Default: Empty string.
    :param str classname: Element's class, does not need to be unique per document. Default: Empty string.
    """       
    
    def __init__(self, id="", classname=""):
        super().__init__(id, classname)
    
    def __repr__(self):
        self._unpack_children()
        return (
            f'<select id="{self._id}" class="{self._classname}">'
            f'\n{self._unpacked_children}\n</select>'
        )

class Option(Element):
    """
    Class represents the <option> tag object of the HTML document.
    Multiple instances of this class may be created in document.
    :param str value: Element's value to be sent to the server.
    :param str content: Content to be placed inside the element's tags.
    :param str id: Element's id, must be unique per document. Default: Empty string.
    :param str classname: Element's class, does not need to be unique per document. Default: Empty string.
    """       
    
    def __init__(self, value, content, id="", classname=""):
        super().__init__(id, classname)
        self._value = value
        self._content = content
    
    def __repr__(self):
        return f'<option id="{self._id}" class="{self._classname}" value="{self._value}">{self._content}</option>'

class Anchor(Element):
    """
    Class represents the <a> tag object of the HTML document.
    Multiple instances of this class may be created in document.
    :param str href: URL address.
    :param str content: Content to be placed inside the element's tags.
    """      

    def __init__(self, href, content, id="", classname=""):
        super().__init__(id, classname)
        self._href = href
        self._content = content
    
    def __repr__(self):
        return f'<a id="{self._id}" class="{self._classname}" href="{self._href}">{self._content}</a>'


class Image(Element):
    """
    Class represents the <img> tag object of the HTML document.
    Multiple instances of this class may be created in document.
    :param str str: Source of the image, an URL address.
    :param str alt: Alternative text description of the image.
    :param str id: Element's id, must be unique per document. Default: Empty string.
    :param str classname: Element's class, does not need to be unique per document. Default: Empty string.
    """   
    def __init__(self, src, alt, id="", classname=""):
        super().__init__(id, classname)
        self._src = src
        self._alt = alt

    def __repr__(self):
        self._unpack_children()
        return f'<img id="{self._id}" class="{self._classname}" src="{self._src}" alt="{self._alt}" />'


class Division(Element):
    """
    Class represents the <div> tag object of the HTML document.
    Multiple instances of this class may be created in document.
    :param str id: Element's id, must be unique per document. Default: Empty string.
    :param str classname: Element's class, does not need to be unique per document. Default: Empty string.
    """       

    def __init__(self, id="", classname=""):
        super().__init__(id, classname)

    def __repr__(self):        
        self._unpack_children()
        return f'<div id="{self._id}">\n{self._unpacked_children}\n</div>'


class Form(Element):
    """
    Class represents the <form> tag object of the HTML document.
    Multiple instances of this class may be created in document.
    :param str action: URL where to send the form-data upon form submit.
    :param str method: HTTP method to use when sending the form data. Valid values are either "get" or "post".
    :param str id: Element's id, must be unique per document. Default: Empty string.
    :param str classname: Element's class, does not need to be unique per document. Default: Empty string.
    """       
    
    def __init__(self, action, method, id="", classname=""):
        super().__init__(id, classname)
        self._action = action
        self._method = method
    
    def __repr__(self):
        self._unpack_children()
        return (
            f'<form id="{self._id}" class="{self._classname}" action="{self._action} method="{self._method}">'
            f'\n{self._unpacked_children}\n</form>'
        )
    

class Label(Element):
    """
    Class represents the <element> tag object of the HTML document.
    Multiple instances of this class may be created in document.
    :param str content: Content to be placed inside the element's tags.
    :param str id: Element's id, must be unique per document. Default: Empty string.
    :param str classname: Element's class, does not need to be unique per document. Default: Empty string.
    """       

    def __init__(self, content, id="", classname=""):
        super().__init__(id, classname)
        self._content = content

    def __repr__(self):        
        self._unpack_children()
        return f'<label id="{self._id}" class="{self._classname}">{self._content}</label>'  