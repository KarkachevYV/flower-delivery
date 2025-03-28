document.addEventListener('DOMContentLoaded', () => {
  console.log("Скрипты подключены!");
});

window.addEventListener('resize', function() {
  const table = document.querySelector('table');
  if (window.innerWidth < 768) {
      // Применить стили или изменить таблицу
  } else {
      // Вернуть обычные стили
  }
});