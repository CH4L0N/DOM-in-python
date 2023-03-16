class HtmlDocument:
    """
    Class represents the entire HTML document, i.e. contents within the <html> tag object.
    Only 1 instance of this class should be created per document.
    """

    def __init__(self):
        from head_elements import Head
        from body_elements import Body
        self.head = Head()
        self.body = Body()

    def __repr__(self):
        return (
            "<!DOCTYPE html>\n"
            "<html>\n"
            f"{str(self.head)}\n"
            f"{str(self.body)}\n"
            "</html>"
        )

    def save_document(self):
        """
        Open a file named "generated_document.html" in write mode ("w").
        The file object returned by open() function is assigned to "file" variable.
        String representation of the main HTML object is saved into the file.
        The resulting file is saved into the same directory as the rest of the code files.
        Note: "with" keyword ensures that the file is properly closed after it is written.
        """
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "generated_doc.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(self))

