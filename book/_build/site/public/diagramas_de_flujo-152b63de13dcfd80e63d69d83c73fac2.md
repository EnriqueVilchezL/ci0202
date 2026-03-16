<!DOCTYPE html>
<html>
<head>
<style>
  #loader {
    position: fixed;
    inset: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background: white;
    z-index: 9999;
  }

  .spinner {
    width: 50px;
    height: 50px;
    border: 6px solid #ddd;
    border-top: 6px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    100% { transform: rotate(360deg); }
  }

  iframe {
    width: 100%;
    height: 100vh;
    border: none;
    display: none; /* hidden until loaded */
  }
</style>
</head>
<body>

<div id="loader">
  <div class="spinner"></div>
</div>

<iframe 
  id="pdfFrame"
  src="https://cdn.jsdelivr.net/gh/EnriqueVilchezL/ci0202@main/book/0_diagramas_de_flujo/diagramas_de_flujo.pdf"
  onload="hideLoader()">
</iframe>

<script>
  function hideLoader() {
    document.getElementById("loader").style.display = "none";
    document.getElementById("pdfFrame").style.display = "block";
  }
</script>

</body>
</html>