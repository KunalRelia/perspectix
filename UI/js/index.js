var source_path = '/views/' + source + '.html';
function loadjsfile(filename) {
    var fileref = document.createElement('script');
    fileref.setAttribute("type", "text/javascript");
    fileref.setAttribute("src", '/js/' + filename);
    if (typeof fileref !== "undefined") {
        document.getElementsByTagName("body")[0].appendChild(fileref);
    }
}
function loadcssfile(filename, filetype) {
    var fileref = document.createElement("link");
    fileref.setAttribute("rel", "stylesheet");
    fileref.setAttribute("type", "text/css");
    fileref.setAttribute("href", '/views/' + filename);
    if (typeof fileref !== "undefined") {
        document.getElementsByTagName("head")[0].appendChild(fileref);
    }
}
function loadfile(filename, filetype) {
    if (filetype === "js") { //if filename is a external JavaScript file
        loadjsfile(filename);
    } else if (filetype === "css") { //if filename is an external CSS file
        loadcssfile(filename);
    }
}

$(document).ready(function () {
    $.get(source_path, function (data) {
        $(data).appendTo("#map");
    });
    loadfile(source + '.js', "js"); //dynamically load and add this .js file
    loadfile(source + '.css', "css"); ////dynamically load and add this .css file
});