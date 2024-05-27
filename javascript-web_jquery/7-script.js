//JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character

let charName;
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  charName = data.name;
  $('DIV#character').text(charName);
});
