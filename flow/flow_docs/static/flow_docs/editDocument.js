let document_id;
document.addEventListener('DOMContentLoaded', function() {
    document_id = document.querySelector('#doc-title').getAttribute('data-id');
    document.querySelector('#share-button').addEventListener('click', showShare);
});

//When the document is initally loaded the input and output panels need to be updated
//This function uses an API call to get the document details from the id
document.addEventListener('buildEvent', function () {
    let body;
    fetch('/documents/' + document_id)
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log(data);
        body = data['body'];
        input = document.querySelector('#input-textarea');
        input.value = body;
        output = document.querySelector('#new-output-panel');
        output.innerHTML = sourceToHtml(body);
    });
});

//overlay is a html element that fades the screen
//the save popup will appear when the saved button is pressed
function showSave() {
    document.querySelector('#overlay').style.display = 'block';
    document.querySelector('#save-popup').style.display = 'block';
};


//If the user specified a title the function will update the document with 
//the new body and the new title
//if no title is specified it will only update the body
function closeSave() {
    const title = document.querySelector('#title-input').value;
    const body = document.querySelector('#input-textarea').value;
    if(title) {
        fetch('/documents/' + document_id, {
            method: 'PUT',
            body: JSON.stringify({
                title: title,
                body: body
            })
        });
    }
    else {
        fetch('/documents/' + document_id, {
            method: 'PUT',
            body: JSON.stringify({
                body: body
            })
        });
    }
    if(title != "") {
        document.querySelector('#doc-title').innerHTML = title;
    }
    document.querySelector('#overlay').style.display = 'none';
    document.querySelector('#save-popup').style.display = 'none';
}

function showShare() {
    document.querySelector('#overlay').style.display = 'block';
    document.querySelector('#share-popup').style.display = 'block';
}

//if there is no input in the text area an alert will appear
//The function will then send an API request to create the new Viewer objects
function closeShare() {
    const users = document.querySelector('#share-input').value;
    if (!users) {
        alert("Please enter an email");
    }
    else { 
        const canEdit = document.querySelector('#edit-checkbox').checked;

        fetch('/share/' + document_id, {
            method: 'POST',
            body: JSON.stringify({
                users: users,
                can_edit: canEdit
            })
        });

        document.querySelector('#overlay').style.display = 'none';
        document.querySelector('#share-popup').style.display = 'none';
    }
}
