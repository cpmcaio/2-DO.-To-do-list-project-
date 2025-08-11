document.addEventListener('DOMContentLoaded', () => {

    const API_URL = 'http://127.0.0.1:8000';
    
    const taskListContainer = document.getElementById('task-list-container');
    const newTaskInput = document.getElementById('new-task-input');
    const addTaskBtn = document.getElementById('add-task-btn');

    async function fetchTasks() {
        try {
            const response = await fetch(`${API_URL}/tarefas/`);
            if (!response.ok) throw new Error('Não foi possível buscar as tarefas.');
            const tasks = await response.json();
            
            taskListContainer.innerHTML = '';
            tasks.forEach(task => {
                const taskElement = createTaskElement(task);
                taskListContainer.appendChild(taskElement);
            });
        } catch (error) {
            console.error('Erro:', error);
        }
    }

    function createTaskElement(task) {
        const li = document.createElement('li');
        li.className = 'task-item';
        li.dataset.id = task.id;
        if (task.concluido) {
            li.classList.add('completed');
        }

        const checkbox = document.createElement('div');
        checkbox.className = 'checkbox';
        checkbox.textContent = '✔';
        checkbox.addEventListener('click', () => toggleTaskStatus(task, li));

        const title = document.createElement('span');
        title.className = 'task-title';
        title.textContent = task.titulo;

        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'delete-btn';
        deleteBtn.innerHTML = '&#128465;';
        deleteBtn.addEventListener('click', () => deleteTask(task.id, li));
        
        li.appendChild(checkbox);
        li.appendChild(title);
        li.appendChild(deleteBtn);

        return li;
    }

    async function addTask() {
        const titulo = newTaskInput.value;
        if (!titulo) {
            alert('Por favor, digite um título para a tarefa.');
            return;
        }

        try {
            const response = await fetch(`${API_URL}/tarefas/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ titulo: titulo, concluido: false })
            });
            if (!response.ok) throw new Error('Falha ao criar tarefa.');
            newTaskInput.value = '';
            fetchTasks();
        } catch (error) {
            console.error('Erro ao adicionar tarefa:', error);
        }
    }

    async function toggleTaskStatus(task, taskElement) {
        const isCompleted = !taskElement.classList.contains('completed');
        try {
            const response = await fetch(`${API_URL}/tarefas/${task.id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ titulo: task.titulo, concluido: isCompleted })
            });
            if (!response.ok) throw new Error('Falha ao atualizar tarefa.');
            taskElement.classList.toggle('completed');
        } catch (error) {
            console.error('Erro ao atualizar tarefa:', error);
        }
    }

    async function deleteTask(taskId, taskElement) {
        try {
            const response = await fetch(`${API_URL}/tarefas/${taskId}`, {
                method: 'DELETE'
            });
            if (!response.ok) throw new Error('Falha ao deletar tarefa.');
            taskElement.remove();
        } catch (error) {
            console.error('Erro ao deletar tarefa:', error);
        }
    }

    addTaskBtn.addEventListener('click', addTask);
    fetchTasks();
});