document.addEventListener("DOMContentLoaded", function() {
    const listMoviesElement = document.querySelector("#list_movies");
    
    fetch("https://swapi-api.hbtn.io/api/films/?format=json")
        .then(response => response.json())
        .then(data => {
            if (listMoviesElement) {
                data.results.forEach(film => {
                    const listItem = document.createElement("li");
                    listItem.textContent = film.title;
                    listMoviesElement.appendChild(listItem);
                });
            }
        })
        .catch(error => {
            console.error("Error fetching the movies data:", error);
        });
});
