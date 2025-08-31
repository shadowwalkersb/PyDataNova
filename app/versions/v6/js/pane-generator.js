// Dynamically generate backend panes for v6
const backends = [
  { id: 'fastapi', title: 'FastAPI' },
  { id: 'flask', title: 'Flask' }
];

backends.forEach(({ id, title }) => {
  const pane = document.createElement('div');
  pane.className = 'pane';
  pane.id = `${id}-pane`;

  pane.innerHTML = `
    <h2>${title}</h2>

    <div id="${id}-root">Root</div>

    <div id="${id}-users">Loading Users...</div>
    <form id="${id}-user-form">
      <input type="text" name="first" placeholder="First Name" required>
      <input type="text" name="last" placeholder="Last Name" required>
      <button type="submit">Add User</button>
    </form>

    <div id="${id}-items">Loading Items...</div>
    <form id="${id}-item-form">
      <input type="text" name="name" placeholder="Item" required>
      <input type="text" name="category" placeholder="Category" required>
      <input type="number" name="price" placeholder="Price" required>
      <input type="number" name="owner_id" placeholder="Owner ID" required>
      <button type="submit">Add Item</button>
    </form>
  `;

  document.body.appendChild(pane);

});
