import React, { useCallback } from 'react';
import { DragDropContext, Droppable, Draggable } from '@dnd-kit/core';
import { arrayMove, SortableContext, verticalListSortingStrategy } from '@dnd-kit/sortable';
import Column from './Column';
import { useKanban } from '../context/KanbanContext';
import { restrictToVerticalAxis } from '@dnd-kit/utilities';

function Board() {
  const { state, reorderColumns } = useKanban();

  const handleDragEnd = useCallback((event) => {
    const { active, over } = event;
    if (over && active.id !== over.id) {
      const oldIndex = state.columns.findIndex(col => col.id === active.id);
      const newIndex = state.columns.findIndex(col => col.id === over.id);
      const newColumns = arrayMove(state.columns, oldIndex, newIndex);
      reorderColumns(newColumns);
    }
  }, [state.columns, reorderColumns]);

  return (
    <div className="board">
      <DragDropContext onDragEnd={handleDragEnd}>
        <Droppable droppableId="all-columns" type="column">
          {(provided) => (
            <div
              className="board-columns"
              ref={provided.innerRef}
              {...provided.droppableProps}
            >
              <SortableContext
                items={state.columns.map(col => col.id)}
                strategy={verticalListSortingStrategy}
              >
                {state.columns.map((column, index) => (
                  <Draggable key={column.id} id={column.id}>
                    {(provided, snapshot) => (
                      <div
                        ref={provided.innerRef}
                        {...provided.draggableProps}
                        {...provided.dragHandleProps}
                        style={{
                          ...provided.draggableProps.style,
                          opacity: snapshot.isDragging ? 0.8 : 1
                        }}
                      >
                        <Column
                          column={column}
                          tasks={state.tasks}
                          index={index}
                        />
                      </div>
                    )}
                  </Draggable>
                ))}
              </SortableContext>
              {provided.placeholder}
            </div>
          )}
        </Droppable>
      </DragDropContext>
    </div>
  );
}

export default Board;