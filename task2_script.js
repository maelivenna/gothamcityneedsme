const form = document.getElementById('todo-form');
const input = document.getElementById('todo-input');
const list = document.getElementById('todo-list');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const li = document.createElement('li');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';

    const text = document.createElement('span');
    text.textContent = input.value;

    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';

    checkbox.addEventListener('change', () => {
        text.classList.toggle('done');
    });

    deleteBtn.addEventListener('click', () => {
        li.remove();
    });

    li.append(checkbox, text, deleteBtn);
    list.appendChild(li);

    input.value = '';
});
