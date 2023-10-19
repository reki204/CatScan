function previewImage(input) {
  if (input.files && input.files[0]) {
    const reader = new FileReader();

    reader.onload = (e) => {
      document.querySelector('#preview').src = e.target.result;
    };

    reader.readAsDataURL(input.files[0]);
  }
};
