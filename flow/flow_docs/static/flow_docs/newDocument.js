//the overlay is an html element that covers the entire screen and gives the
//effect of a fade. 
//The popup is the box that appears for users to specify the title

function showSave() {
    document.querySelector('#overlay').style.display = 'block';
    document.querySelector('#save-popup').style.display = 'block';
};

function closeSave() {
    const title = document.querySelector('#title-input').value;
    if (!title) {
        alert("Please enter a title before saving")
    }
    else {
        document.querySelector('#overlay').style.display = 'none';
        document.querySelector('#save-popup').style.display = 'none';
        saveDocument(title);
    }
}

function saveDocument(title) {
    const body = document.querySelector('#input-textarea').value;
    fetch('/documents', {
        method: 'POST',
        body: JSON.stringify({
            title: title,
            body: body,
        })
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log(data);
        window.location.href = "/edit/" + data['id'];
    });
};

