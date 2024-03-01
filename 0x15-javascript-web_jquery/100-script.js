let head = document.querySelector('head');
let newScript = document.createElement('script', {
  "defer": "defer",
  "type": "text/javascript"
});
newScript.textContent = " let header = document.querySelector('header');\
header.style.color = '#FF0000'"
head.appendChild(newScript);
