document.addEventListener('DOMContentLoaded', () => {
    const plantList = document.getElementById('plant-list');
    const gardenCanvas = document.getElementById('garden-canvas');

    let draggedPlant = null;

    // Make plant items draggable
    document.querySelectorAll('.plant-item').forEach(item => {
        item.addEventListener('dragstart', (e) => {
            draggedPlant = e.target;
            e.dataTransfer.setData('text/plain', draggedPlant.dataset.id);
        });
    });

    // Allow the garden canvas to accept drop events
    gardenCanvas.addEventListener('dragover', (e) => {
        e.preventDefault();
    });

    gardenCanvas.addEventListener('drop', (e) => {
        e.preventDefault();
        const plantId = e.dataTransfer.getData('text/plain');
        const plantElement = document.querySelector(`.plant-item[data-id="${plantId}"]`);

        if (plantElement) {
            const x = e.offsetX;
            const y = e.offsetY;

            const plantedItem = document.createElement('div');
            plantedItem.classList.add('planted-item');
            plantedItem.style.left = `${x}px`;
            plantedItem.style.top = `${y}px`;
            plantedItem.innerHTML = `
                <img src="${plantElement.querySelector('img').src}" alt="${plantElement.querySelector('span').textContent}">
                <span>${plantElement.querySelector('span').textContent}</span>
            `;

            gardenCanvas.appendChild(plantedItem);
        }
    });
});