from html_document import HtmlDocument
from head_elements import Meta, Title
from body_elements import Input, Select, Option, Anchor, Image, Division, Form, Label

# STEP 1: Creation of the main object, which also creates the Head and Body objects
html_document = HtmlDocument()


# STEP 2: Head definition
meta_charset = Meta()
html_document.head.add_child(meta_charset)

title = Title("Aplikace: Přihlašovací formulář")
html_document.head.add_child(title)


# STEP 3: Body definition
div = Division("login_form_division")
html_document.body.add_child(div)

img = Image("./img/login_form_logo.png", "Login form's logo in cyan colour")
div.add_child(img)

form = Form("/login_action_page.php", "post", "login")
div.add_child(form)

label_username = Label("Uživatelské jméno:")
form.add_child(label_username)

input_username = Input("text", "username", "Honza")
form.add_child(input_username)

label_password = Label("Heslo:")
form.add_child(label_password)

input_password = Input("password", "password")
form.add_child(input_password)

label_role = Label("Role:")
form.add_child(label_role)

select_role = Select()
form.add_child(select_role)

option_user = Option("user", "Uživatel")
select_role.add_child(option_user)

option_admin = Option("admin", "Administrátor")
select_role.add_child(option_admin)

input_submit = Input("submit", "Odeslat", "login_form_submit")
form.add_child(input_submit)

link_go_back = Anchor("index.html", "Jít zpět")
div.add_child(link_go_back)

# STEP 4: Testing whether the output matches expected result
print(html_document)


# STEP 5: Saving the entire HTML document to a file
html_document.save_document()