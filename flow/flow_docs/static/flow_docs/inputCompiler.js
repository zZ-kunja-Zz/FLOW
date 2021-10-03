function NewDocument() {
    const [input, setInput] = React.useState("");
    function updateText(event) {
        let text = event.target.value;
        setInput(text);
        //converts the input code to HTML
        text = sourceToHtml(text);
        document.querySelector('#new-output-panel').innerHTML = text;
    }
    //textarea for user to write the code in
    //button to save the document
    //panel to display the output
    return (
        <div id="new-document">
            <div className="new-panel" id="new-input-panel">
                <textarea spellCheck="false" id="input-textarea" onChange={updateText} value={input}/>
                <button onClick={showSave} id="save-button">Save</button>
            </div>
            <div className="new-panel" id="new-output-panel">
            </div>
        </div>
    )
};
//renders the component above
ReactDOM.render(<NewDocument />, document.querySelector('#new-document-div'))

//When the page loads the documents previous changes need to be displayed to the input and output
//when this function is called the editDocument.js file knows to update input and output fields
const buildEvent = new Event('buildEvent');
document.dispatchEvent(buildEvent);

