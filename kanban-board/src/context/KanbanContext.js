import React, { createContext, useContext, useReducer, useCallback } from 'react';

const KanbanContext = createContext(null);

const initialState = {
  columns: [
    {
      id: 'col-1',
      title: 'To Do',
      taskIds: ['task-1', 'task-2']
    },
    {
      id: 'col-2',
      title: 'In Progress',
      taskIds: ['task-3']
    },
    {
      id: 'col-3',
      title: 'Done',
      taskIds: ['task-4']
    }
  ],
  tasks: {
    'task-1': { id: 'task-1', content: 'Set up project structure' },
    'task-2': { id: 'task-2', content: 'Create initial wireframes' },
    'task-3': { id: 'task-3', content: 'Implement drag and drop' },
    'task-4': { id: 'task-4', content: 'Write documentation' }
  }
};

function kanbanReducer(state, action) {
  switch (action.type) {
    case 'ADD_TASK': {
      const { taskId, content, columnId } = action.payload;
      return {
        ...state,
        tasks: {
          ...state.tasks,
          [taskId]: { id: taskId, content }
        },
        columns: state.columns.map(col =>
          col.id === columnId
            ? { ...col, taskIds: [...col.taskIds, taskId] }
            : col
        )
      };
    }
    case 'MOVE_TASK': {
      const { taskId, sourceColId, destColId, newTaskIds } = action.payload;
      return {
        ...state,
        columns: state.columns.map(col => {
          if (col.id === sourceColId) {
            return { ...col, taskIds: col.taskIds.filter(id => id !== taskId) };
          }
          if (col.id === destColId) {
            return { ...col, taskIds: newTaskIds };
          }
          return col;
        })
      };
    }
    case 'REORDER_TASKS': {
      const { columnId, newTaskIds } = action.payload;
      return {
        ...state,
        columns: state.columns.map(col =>
          col.id === columnId ? { ...col, taskIds: newTaskIds } : col
        )
      };
    }
    case 'REORDER_COLUMNS': {
      return {
        ...state,
        columns: action.payload
      };
    }
    case 'EDIT_TASK': {
      const { taskId, content } = action.payload;
      return {
        ...state,
        tasks: {
          ...state.tasks,
          [taskId]: { ...state.tasks[taskId], content }
        }
      };
    }
    case 'DELETE_TASK': {
      const { taskId, columnId } = action.payload;
      return {
        ...state,
        tasks: Object.fromEntries(
          Object.entries(state.tasks).filter(([id]) => id !== taskId)
        ),
        columns: state.columns.map(col =>
          col.id === columnId
            ? { ...col, taskIds: col.taskIds.filter(id => id !== taskId) }
            : col
        )
      };
    }
    default:
      return state;
  }
}

export function KanbanProvider({ children }) {
  const [state, dispatch] = useReducer(kanbanReducer, initialState);

  const addTask = useCallback((taskId, content, columnId) => {
    dispatch({ type: 'ADD_TASK', payload: { taskId, content, columnId } });
  }, []);

  const moveTask = useCallback((taskId, sourceColId, destColId, newTaskIds) => {
    dispatch({ type: 'MOVE_TASK', payload: { taskId, sourceColId, destColId, newTaskIds } });
  }, []);

  const reorderTasks = useCallback((columnId, newTaskIds) => {
    dispatch({ type: 'REORDER_TASKS', payload: { columnId, newTaskIds } });
  }, []);

  const reorderColumns = useCallback((newColumns) => {
    dispatch({ type: 'REORDER_COLUMNS', payload: newColumns });
  }, []);

  const editTask = useCallback((taskId, content) => {
    dispatch({ type: 'EDIT_TASK', payload: { taskId, content } });
  }, []);

  const deleteTask = useCallback((taskId, columnId) => {
    dispatch({ type: 'DELETE_TASK', payload: { taskId, columnId } });
  }, []);

  return (
    <KanbanContext.Provider value={{
      state, addTask, moveTask, reorderTasks, reorderColumns, editTask, deleteTask
    }}>
      {children}
    </KanbanContext.Provider>
  );
}

export function useKanban() {
  const context = useContext(KanbanContext);
  if (!context) {
    throw new Error('useKanban must be used within a KanbanProvider');
  }
  return context;
}