//JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
//All movie titles must be list in the HTML tag UL#list_movies
//You must use the jQuery API
let movieTitle;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (movieTitle of data.results) {
    title = data.results[i].title;
    $('UL#list_movies').append(`<li>${title}</li>`);
  }
});
