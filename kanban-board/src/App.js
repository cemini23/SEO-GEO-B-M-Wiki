import React, { useState } from 'react';
import Board from './components/Board';
import { KanbanProvider } from './context/KanbanContext';

function App() {
  return (
    <KanbanProvider>
      <div className="App">
        <Board />
      </div>
    </KanbanProvider>
  );
}

export default App;