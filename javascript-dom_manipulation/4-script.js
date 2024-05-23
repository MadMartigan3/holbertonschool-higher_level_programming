document.querySelector('#add_item').addEventListener('click', function () {
  const list = document.querySelector('.my_list');
  const item = document.createElement('li');
  item.appendChild(document.createTextNode('Item'));
  list.appendChild(item);
});
