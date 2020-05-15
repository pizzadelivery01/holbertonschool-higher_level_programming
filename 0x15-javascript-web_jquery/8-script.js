// gets starwars
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function SW(data) {
let movies = data.results;
for (let i in movies) {
    $('#list_movies').append('<li>' + movies[i].title + '</li>');
}   
});