const words = {
    A: ["Ana", "Arbore"],
    E: ["Elena", "Energie"],
    I: ["Ion", "India"],
    O: ["Oscar", "Ochi"],
    U: ["Ungaria", "Urs"],
    a: ["aer", "arbore"],
    e: ["energie", "efort"],
    i: ["inel", "ionut"],
    o: ["ochi", "omulet"],
    u: ["urs", "umbra"]
};

let selectedVowel = "";
let score = 0;

// Verificăm dacă scorul minim pentru deblocare a fost atins
function checkAccess() {
    const overallScore = localStorage.getItem("overallScore") || 0;
    if (overallScore < 30) {
        alert("Trebuie să obții 30 de puncte la jocul anterior pentru a accesa acest joc!");
        window.location.href = "/"; // Redirecționează la pagina principală
    }
}

// Generăm cuvintele
function generateWords() {
    const wordsContainer = document.getElementById("words-container");
    wordsContainer.innerHTML = "";

    Object.entries(words).forEach(([vowel, wordList]) => {
        wordList.forEach(word => {
            const wordButton = document.createElement("button");
            wordButton.textContent = word;
            wordButton.className = "word-button";
            wordButton.setAttribute("data-vowel", vowel);
            wordButton.addEventListener("click", () => checkMatch(word, vowel));
            wordsContainer.appendChild(wordButton);
        });
    });
}

// Selectăm o vocală
function selectVowel(vowel) {
    selectedVowel = vowel;
    const feedbackElement = document.getElementById("feedback");
    feedbackElement.textContent = `Ai selectat vocala: ${vowel}`;
    feedbackElement.style.color = "blue";
}

// Verificăm asocierea cuvântului cu vocala
function checkMatch(word, vowel) {
    const feedbackElement = document.getElementById("feedback");
    const scoreElement = document.getElementById("score");
    const correctSound = document.getElementById("correct-sound");
    const wrongSound = document.getElementById("wrong-sound");

    if (selectedVowel === vowel) {
        score++;
        feedbackElement.textContent = `Bravo! ${word} începe cu ${vowel}!`;
        feedbackElement.style.color = "green";
        correctSound.play();
    } else {
        feedbackElement.textContent = `Mai încearcă! ${word} nu începe cu ${selectedVowel}.`;
        feedbackElement.style.color = "red";
        wrongSound.play();
    }

    scoreElement.textContent = `Scor: ${score}`;
}

// Adăugăm evenimente și verificăm accesul
document.addEventListener("DOMContentLoaded", () => {
    checkAccess();

    const vowelButtons = document.querySelectorAll(".vowel-button");
    vowelButtons.forEach(button => {
        button.addEventListener("click", () => {
            const vowel = button.getAttribute("data-vowel");
            selectVowel(vowel);
        });
    });

    generateWords();
});
