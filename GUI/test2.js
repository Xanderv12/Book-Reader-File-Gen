


        function createFile() {
        // Create a Blob object with the text content
            var blob = new Blob([x], { type: "text/plain" });

        // Create a temporary link element
            var link = document.createElement("a");
            link.href = URL.createObjectURL(blob);
            link.download = "example.txt"; // Name of the file

        // Trigger the download
            document.body.appendChild(link);
            link.click();

        // Clean up
            document.body.removeChild(link);
            URL.revokeObjectURL(link.href);
            }



/** 
var y = document.getElementById("Directory2").value;
var z = document.getElementById("Directory3").value;

var title = document.getElementById("title").value;
var pages = document.getElementById("Pages").value;
var height = document.getElementById("Height").value;
var width = document.getElementById("Width").value;
var base = document.getElementById("Base").value;
*/