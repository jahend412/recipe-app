// Adding JavaScript code to create a search bar that filters recipes by name
function search_recipe() {
    let input = document.getElementById('searchbar').value
    input = input.toLowerCase();  // Converting to lowercase to make it case insensitive
    let recipes = document.getElementsByClassName('recipe_searched');  // Stores recipe list on database in a variable

    let recipe_box = document.getElementsByClassName('search_results');
    recipe_box[0].style.display = "block";

    for (i = 0; i < recipes.length; i++) {
        if (!recipes[i].innerHTML.toLowerCase().includes(input)) {             // If the recipe name does not match the search input, hide it
            recipes[i].style.display = "none";
        }
        else {
            recipes[i].style.display = "block";                                 // If the recipe name matches the search input, show it
        }
    }
    if (input == "") {
        recipe_box[0].style.display = "none";                               // If the search input is empty, hide the search results box
    }
}