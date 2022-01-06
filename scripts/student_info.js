const profile ={}
let input = document.getElementById("files")

input.addEventListener("change", function(event) {
    //console.log(input.files)
    let files = event.target.files;
    console.log(files)
    for (let text of files){
        text.split('_')
        const reader = new FileReader()
        reader.readAsText(text)
        reader.onload  = function (){
            console.log(reader.result)
        }
    }
}, false);
//webkitRelativePath