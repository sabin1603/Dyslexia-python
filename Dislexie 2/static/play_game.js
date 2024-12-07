let score = 0;
let correctVowel = "";

// Funcție pentru actualizarea întrebării
function updateQuestion() {
    fetch('/get-random-vowel')
        .then(response => response.json())
        .then(data => {
            correctVowel = data.correct_vowel;
            document.getElementById("question").textContent = `Alege vocala: ${correctVowel}`;
            const feedbackElement = document.getElementById("feedback");
            feedbackElement.textContent = ""; // Resetare feedback
        });
}

// Funcție pentru verificarea răspunsului
function checkAnswer(selectedVowel) {
    const feedbackElement = document.getElementById("feedback");
    const scoreElement = document.getElementById("score");

    const correctSound = document.getElementById("correct-sound");
    const wrongSound = document.getElementById("wrong-sound");

    if (selectedVowel === correctVowel) {
        score++;
        scoreElement.textContent = `Scor: ${score}`;
        feedbackElement.textContent = "Bravo! Ai răspuns corect!";
        feedbackElement.style.color = "green";
        correctSound.play();
    } else {
        feedbackElement.textContent = "Mai încearcă!";
        feedbackElement.style.color = "red";
        wrongSound.play();
    }

    // Menține mesajul pe ecran timp de 3 secunde înainte de a actualiza întrebarea
    setTimeout(() => {
        feedbackElement.textContent = ""; // Golește feedback-ul
        updateQuestion(); // Actualizează întrebarea
    }, 1200); // 3000 ms = 3 secunde
}

// Adaugă evenimente pe butoane după ce pagina s-a încărcat
document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".vowel-button");
    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const selectedVowel = button.getAttribute("data-vowel");
            checkAnswer(selectedVowel);
        });
    });

    updateQuestion();

function checkAnswer(selectedVowel) {
    const correctVowel = ...; // Obține vocala corectă
    const feedbackElement = document.getElementById("feedback");
    const scoreElement = document.getElementById("score");

    if (selectedVowel === correctVowel) {
        score++;
        localStorage.setItem("overallScore", score); // Salvează scorul global
        feedbackElement.textContent = "Bravo! Ai ales corect!";
    } else {
        feedbackElement.textContent = "Mai încearcă! Nu ai ales corect.";
    }

    scoreElement.textContent = `Scor: ${score}`;
}

});
