function createTestExit() {
    let createTestBox = document.getElementsByClassName('createTest')[0];
    createTestBox.style.display = 'none';
    let testGrid = document.getElementsByClassName('tests-grid')[0];
    testGrid.style.display = 'grid';
}

function displayCreateTest() {
    let testGrid = document.getElementsByClassName('tests-grid')[0];
    testGrid.style.display = 'none';
    let createTestBox = document.getElementsByClassName('createTest')[0];
    createTestBox.style.display = 'block';
}

function addQuestion() {
    const questionDiv = `<div class="createTest-box question-flex">
    <label for="question-textarea">Question</label>
    <textarea class="question-textarea" cols="50" rows="10"></textarea>
    <button class="question-delete" onclick="deleteQuestion(event)">x</button>
    </div>`;

    let createTestBox = document.getElementsByClassName('questions')[0];
    createTestBox.insertAdjacentHTML('beforeend', questionDiv);
}

function deleteQuestion(event) {
    const button = event.target;
    const div = button.closest('.createTest-box');
    div.remove();
}


