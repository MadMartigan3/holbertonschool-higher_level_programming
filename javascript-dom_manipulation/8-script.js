document.addEventListener("DOMContentLoaded", function() {
    const helloElement = document.querySelector("#hello");
    
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
        .then(response => response.json())
        .then(data => {
            if (helloElement) {
                helloElement.textContent = data.hello;
            }
        })
        .catch(error => {
            console.error("Error fetching the hello translation:", error);
        });
});
