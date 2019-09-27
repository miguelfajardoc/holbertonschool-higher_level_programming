$.getJSON('https://swapi.co/api/people/5/?format=json', function(ch) {
  $('#character').text(ch.name);
});
