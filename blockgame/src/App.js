import React, { useState, useEffect } from 'react';

const MineSweeperGame = ({ rows, cols, mines }) => {
  const [grid, setGrid] = useState([]);
  const [gameOver, setGameOver] = useState(false);

  useEffect(() => {
    initializeGrid();
  }, []);

  const initializeGrid = () => {
    const newGrid = Array(rows)
      .fill(null)
      .map(() => Array(cols).fill({ isMine: false, count: 0, isRevealed: false }));

    let minesCount = 0;
    while (minesCount < mines) {
      const randomRow = Math.floor(Math.random() * rows);
      const randomCol = Math.floor(Math.random() * cols);

      if (!newGrid[randomRow][randomCol].isMine) {
        newGrid[randomRow][randomCol].isMine = true;
        minesCount++;
      }
    }

    setGrid(newGrid);
  };

  const handleCellClick = (row, col) => {
    if (gameOver) return;

    const clickedCell = grid[row][col];
    if (clickedCell.isMine) {
      setGameOver(true);
    } else {
      const newGrid = [...grid];
      newGrid[row][col].isRevealed = true;
      setGrid(newGrid);
    }
  };

  const countAdjacentMines = (row, col) => {
    const directions = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
      [1, 1],
      [-1, -1],
      [1, -1],
      [-1, 1],
    ];

    let count = 0;
    for (let i = 0; i < directions.length; i++) {
      const [dx, dy] = directions[i];
      const newRow = row + dx;
      const newCol = col + dy;

      if (
        newRow >= 0 &&
        newRow < rows &&
        newCol >= 0 &&
        newCol < cols &&
        grid[newRow][newCol].isMine
      ) {
        count++;
      }
    }

    return count;
  };

  const renderGrid = () => {
    return grid.map((row, rowIndex) => (
      <div key={rowIndex} className="row">
        {row.map((cell, colIndex) => (
          <div
            key={colIndex}
            className={`cell ${cell.isRevealed ? 'revealed' : ''}`}
            onClick={() => handleCellClick(rowIndex, colIndex)}
          >
            {cell.isRevealed && !cell.isMine && cell.count !== 0 && cell.count}
            {cell.isRevealed && cell.isMine && '💣'}
          </div>
        ))}
      </div>
    ));
  };

  return (
    <div className="minesweeper">
      <h1>Mine Sweeper Game</h1>
      {gameOver && <h2>Game Over!</h2>}
      <div className="grid">{renderGrid()}</div>
    </div>
  );
};

export default MineSweeperGame;
