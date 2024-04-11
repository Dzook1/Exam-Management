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
