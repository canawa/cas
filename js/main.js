<script>
  // Найти элемент div
  const hoverDiv = document.querySelector('.hover-div');
  
  // Найти элемент <i> внутри div
  const icon = hoverDiv.querySelector('i');

  // Добавить обработчик событий
  hoverDiv.addEventListener('mouseenter', () => {
    icon.classList.add('fa-bounce'); // Добавить класс при наведении
  });

  hoverDiv.addEventListener('mouseleave', () => {
    icon.classList.remove('fa-bounce'); // Удалить класс при выходе
  });
</script>
