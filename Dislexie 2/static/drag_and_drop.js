let score = 0;

function generateDragItems() {
    const vowels = ["A", "E", "I", "O", "U"];
    const dragItemsContainer = document.getElementById("drag-items-container");
    dragItemsContainer.innerHTML = ""; // Resetează vocalele

    vowels.forEach(vowel => {
        const dragItem = document.createElement("div");
        dragItem.textContent = vowel;
        dragItem.className = "drag-item";
        dragItem.setAttribute("draggable", true);
        dragItem.setAttribute("data-vowel", vowel);

        // Adaugă evenimentele de drag
        dragItem.addEventListener("dragstart", onDragStart);
        dragItemsContainer.appendChild(dragItem);
    });
}

function onDragStart(event) {
    event.dataTransfer.setData("text/plain", event.target.getAttribute("data-vowel"));
    event.target.classList.add("dragging");
}

function onDragOver(event) {
    event.preventDefault(); // Permite drop-ul
}

function onDrop(event) {
    event.preventDefault();
    const droppedVowel = event.dataTransfer.getData("text/plain");
    const basketVowel = event.target.getAttribute("data-vowel");

    const feedbackElement = document.getElementById("feedback");
    const scoreElement = document.getElementById("score");

    if (droppedVowel === basketVowel) {
        score++;
        feedbackElement.textContent = `Bravo! Ai plasat ${droppedVowel} în coșul corect.`;
        feedbackElement.style.color = "green";
        scoreElement.textContent = `Scor: ${score}`;

        // Eliminăm elementul plasat corect
        const draggedElement = document.querySelector(`.drag-item[data-vowel="${droppedVowel}"]`);
        if (draggedElement) draggedElement.remove();
    } else {
        feedbackElement.textContent = `Mai încearcă! ${droppedVowel} nu aparține coșului ${basketVowel}.`;
        feedbackElement.style.color = "red";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    generateDragItems();

    // Adaugă evenimentele pe coșuri
    const baskets = document.querySelectorAll(".basket");
    baskets.forEach(basket => {
        basket.addEventListener("dragover", onDragOver);
        basket.addEventListener("drop", onDrop);
    });
});
