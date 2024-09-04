// Ensure the DOM is fully loaded before executing scripts
document.addEventListener('DOMContentLoaded', function() {
    // Example functionality: Adding a simple alert when a plant card is clicked
    const plantCards = document.querySelectorAll('.plant-card');

    plantCards.forEach(card => {
        card.addEventListener('click', function() {
            const plantName = this.querySelector('h2').textContent;
            alert(`You clicked on ${plantName}`);
        });
    });

    // Example functionality: Toggle the visibility of plant descriptions
    const plantDescriptions = document.querySelectorAll('.plant-card p');

    plantDescriptions.forEach(description => {
        // Add a click event listener to toggle the description visibility
        description.addEventListener('click', function() {
            this.classList.toggle('hidden');
        });
    });
});
