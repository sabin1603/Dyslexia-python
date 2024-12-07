// Redă un fișier audio bazat pe numele vocalelor
function playSound(vowel) {
    const audio = new Audio(`/static/sounds/${vowel}.mp3`);
    audio.play();
}

// Actualizează textul și culorile feedback-ului în jocurile interactive
function updateFeedback(message, isSuccess) {
    const feedbackElement = document.getElementById('feedback');
    feedbackElement.textContent = message;

    if (isSuccess) {
        feedbackElement.style.color = 'green';
    } else {
        feedbackElement.style.color = 'red';
    }
}

// Generează o nouă întrebare pentru jocurile bazate pe selectarea vocalelor
function generateQuestion(vowels) {
    const questionElement = document.getElementById('question');
    const randomVowel = vowels[Math.floor(Math.random() * vowels.length)];
    questionElement.textContent = `Alege vocala: ${randomVowel}`;
    return randomVowel;
}

// Verifică răspunsul pentru jocurile bazate pe selectarea vocalelor
function checkAnswer(selectedVowel, correctVowel) {
    if (selectedVowel === correctVowel) {
        updateFeedback('Bravo! Ai ales corect!', true);
        return true;
    } else {
        updateFeedback('Mai încearcă!', false);
        return false;
    }
}

// Exemplu de inițializare pentru jocuri (adaugă evenimente pe butoane)
function initGame(vowels) {
    const buttons = document.querySelectorAll('.vowel-button');
    const correctVowel = generateQuestion(vowels);

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const selectedVowel = button.textContent;
            if (checkAnswer(selectedVowel, correctVowel)) {
                setTimeout(() => {
                    initGame(vowels); // Generează o nouă întrebare
                }, 1000); // Așteaptă puțin înainte să actualizezi întrebarea
            }
        });
    });
}
