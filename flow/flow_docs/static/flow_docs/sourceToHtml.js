function sourceToHtml(text) {
    //clean the input so user can't add html or django keywords
    //the symbols are replaced with the html code for the symbols
    text = text.replaceAll(/</g, "&lt;");
    text = text.replaceAll(/>/g, "&gt;");
    text = text.replaceAll(/{/g, "&lcub;");
    text = text.replaceAll(/}/g, "&rcub;");
    //this creates the html needed for titles
    //text = findKeyword(text, "test", "TEST");
    text = findKeyword(text, "title", "<h1 class='document-title'>");
    text = findKeyword(text, "endtitle", "</h1>")
    //creates new paragraph
    text = findKeyword(text, "paragraph", "<p class='document-paragraph'>&emsp;");
    text = findKeyword(text, "endparagraph", "</p>");
    //replacing newl with newline
    text = findKeyword(text, "new", "</br>");
    //replacing newlines with a space
    text = findKeyword(text, "\n", " ");
    return text;
}

//text is the text to search, find is the word to find, replace is what
//to replace it with
//It will only detect words that are surrounded by newlines
function findKeyword(text, find, replace) {
    text = text.replaceAll(RegExp(`(?<=\n)${find}(?=\n)|(?<=^)${find}(?=\n)`, "g"), replace);
    return text;
};