function openModal(imageUrl) {
    var modal = document.getElementById('modal');
    var modalImage = document.getElementById('modalImage');
  
    modalImage.src = imageUrl;
    modal.style.display = 'block';
  }
  
  function closeModal() {
    var modal = document.getElementById('modal');
    modal.style.display = 'none';
  }