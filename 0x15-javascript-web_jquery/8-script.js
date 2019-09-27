$.getJSON('https://swapi.co/api/films/?format=json', function (film) {
  film = film.results;
  for (i of film){
    $('#list_movies').append('<li>' + i.title + '</li>');
  }  
});