document.addEventListener('DOMContentLoaded', function() {
  // File Upload Event Listener
  document.getElementById('file-upload').addEventListener('change', function() {
    // Get the selected file name
    var fileName = this.value.split('\\').pop();
    // Display the selected file name
    document.getElementById('selected-file').innerHTML = fileName;
  });
});
