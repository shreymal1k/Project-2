let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";

// Function to handle a move on the board
function makeMove(index) {
    if (board[index] !== "") return;  // Ignore if the cell is already filled
    board[index] = currentPlayer;
    document.getElementsByClassName('cell')[index].textContent = currentPlayer;

    // Send the updated board to the backend
    fetch(`/move`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            board: board,
            player: currentPlayer
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.winner) {
            document.getElementById("message").textContent = `${data.winner} wins!`;
        } else if (data.draw) {
            document.getElementById("message").textContent = "It's a draw!";
        } else {
            currentPlayer = currentPlayer === "X" ? "O" : "X";
        }
    });
}

// Function to reset the game
function resetGame() {
    board = ["", "", "", "", "", "", "", "", ""];
    currentPlayer = "X";
    document.getElementById("message").textContent = "";
    let cells = document.getElementsByClassName('cell');
    for (let i = 0; i < cells.length; i++) {
        cells[i].textContent = "";
    }

    fetch("/reset", { method: "POST" });
}
