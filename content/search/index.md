+++
title = "Search"
description = "Client-side search. No external servers involved."
weight = -170
css = ["css/search.css"]
showpagemeta = false
+++

<div id="search" class="search-container"></div>

<script src="/pagefind/pagefind-ui.js"></script>

<script>
  window.addEventListener('DOMContentLoaded', (event) => {
    new PagefindUI({
      element: "#search",
      resetStyles: false,
      showSubResults: true, // Shows matches within headings
      showImages: false,    // Set to true if you want post images in results
      translations: {
        placeholder: "Enter your search query here"
      }
    });
  });
</script>

