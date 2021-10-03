IDEA
Flow is a writing tool to make writing faster and more efficient. 
Having every sentence separated by periods is better for reading but harder to edit sentences.
The idea behind flow is that it allows you to write sentences line by line with formatting commands.
It is a combination of programming syntax and LaTeX.

Flow currently has the commands to create newlines, paragraphs and titles.
Since adding new commands is mostly hard coding I didn't add too many.
Flow parses through the document with regular expressions to find keywords.
When it detects a keyword it will inject the neccesary HTML into the input text.
The input and output are handled with react and the output updates in real time.

================================================================================
HOW TO USE THE SITE:

1. Make an account and sign in
2. Click on the documentation tab for a guide on how the syntax works
3. Click on the new tab to create your first document.
4. When you are ready hit save and choose a title
5. You will be taken to the edit url for that document now.
6. Once saved you can now share the document with other users.
7. If you just let someone view they will only be able to access the view url for a page.
8. If not they will be able to go into the edit view for your document.

MOBILE USE:
1. Create some documents on a computer first
2. Log on in mobile view
3. You can now browse all documents shared with you or your saved documents


================================================================================
MODELS:
>User 
    Standard django user model 

>Document 
    Model to store all the documents.
    Properties:
        Owner: the author of the document
        Title: the title of the document
        Body: the "flow source code" of the document
        Timestamp: the time at which it was created

>Viewer
    Model to handle who can view and edit documents
    Properties:
        User: the person who can view/edit the document
        Document: the document which can be viewed or edited
        canEdit: can this person edit the document or simply view

================================================================================
STATIC:

>sourceToHtml.js
    This file converts the "flow source code" into the HTML output.
    It takes a string as input and it returns the updates string.
    I decided to use regular expressions to parse the input as they allow for cleaner code.
    Regular expressions make it easier to write more general code.

>inputCompiler.js
    This is a react component that creates two panels.
    The first panel is the user input and the second is the HTML output.
    It uses sourceToHtml.js to translate the input and whenever onChange is triggered it will
    display the output.

>newDocument.js
    This is the file that loads when you open a new file.
    It controls a popup and the title.
    When the user presses the 'save' button a popup appears.
    This file makes that popup fade the rest of the screen and also handles saving.
    When the user confirms saving the file they input a title which this file sends
    along with the body of the text to an API call which creates the new Document object.
    Once the document is saved you are now taken to the edit page for that document.

>editDocument.js
    This is the file that loads when you edit a file.
    It is very similar to newDocument.js.
    There is a second popup: share
    When you share a document an API call is made to share the document.
    It creates an object in the database with all the users and the document.
    When you save instead of creating a document a POST request is made and it updates
    the title and the body.

>viewDocument.js
    Not every user can edit every document, some can only view.
    viewDocument.js simply converts the input with sourceToHtml.js and puts the output into a div.

>favicon.ico 
    The favicon for the site.

>lowres logo.png   
    Image in the top right of the header bar.

>styles.css
    This and bootstrap control all the CSS in the site.

================================================================================
TEMPLATES:

>all.html 
    For displaying every document available to you.
    On PC it will give you edit links on mobile you just get view links.
    If you don't have permission to edit then you will get a view link as well.

>documentation.html 
    A quick reference for how to write "flow source code".

>edit.html
    HTML page for editing documents

>index.html
    There is nothing on this page for now.

>layout.html
    Controls the header bar and adds the CSS, bootstrap, and React.

>login.html, register.html
    Taken from other projects.

>new.html
    HTML page for creating new documents

>saved.html
    Shows every document you have saved so far.

>view.html 
    HTML page to view a given document

================================================================================
DJANGO PYTHON FILES:

>__init__.py, app.py, manage.py, tests.py, entire inner flow folder
    All of these were either barely changed or stayed the same as default.

>admin.py
    Puts the User, Document and Viewer models into the admin view.

>models.py
    Defines the User, Document and Viewer model.

>urls.py
    Defines all the page URLS and the API routes

================================================================================
VIEWS.PY:

>Index, new, documentation
    These simply return the associated HTML files as no data is needed.

>login_view, logout_view, register
    Taken from previous projects.
    These just allow a user to login, logout and register.

>edit 
    Takes argument document_id.
    It will give the HTML file a list of users who can edit and also the title and document id.

>view
    Takes argument document_id.
    It will give the HTML file a list of users who can view and also the document object.

>share 
    It takes a POST request and it will create a Viewer object for every user that is inputted.

>save
    Takes a POST request and will create a document with the request.user, and inputted title and body.

>saved
    Sorts a list of all saved documents and gives it to HTML file.

>all
    Sorts a list of all saved and viewable documents and gives it to the HTML file.
================================================================================
MOBILE:
*note to grader
I am interested in how you think I could add to the mobile side as I had very little ideas.
*end note

The idea of flow is completely irrelevant when it comes to mobile.
Typing line by line is extremely tedious and it would be faster to use anything else.
In addition it is not often people write on their phone.
That is why I decided to completely strip the editing feature for mobile users.
As a mobile user you are able to view all the documents shared with you or that you have saved.
However you only get view links and you can not edit anything.



