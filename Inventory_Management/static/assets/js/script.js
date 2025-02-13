function searchTable() {
    // Get input value
    var input = document.getElementById("searchInput").value.toLowerCase();
    // Get the table and rows
    var table = document.getElementById("dataTable");
    var rows = table.getElementsByTagName("tr");

    // Loop through all table rows 
    for (var i = 1; i < rows.length; i++) {  
      var cells = rows[i].getElementsByTagName("td");
      var match = false;

      // Loop through each cell to check if it contains 
      for (var j = 0; j < cells.length; j++) {
        if (cells[j]) {
          var cellText = cells[j].innerText.toLowerCase();
          if (cellText==input) {
            match = true;
            break;
          }
        }
      }

      rows[i].style.display = match ? "" : "none";
    }
  }
