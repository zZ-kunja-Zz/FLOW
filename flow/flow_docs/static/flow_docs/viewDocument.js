//compiles the input and puts it into the div
document.addEventListener('DOMContentLoaded', function() {
    const body = document.querySelector('#document-panel-body').getAttribute('data-body');
    const output = sourceToHtml(body);
    document.querySelector('#document-panel-body').innerHTML = output;
});