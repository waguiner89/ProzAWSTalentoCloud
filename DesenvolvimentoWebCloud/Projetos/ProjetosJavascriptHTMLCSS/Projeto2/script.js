const elementoH1 = document.getElementById('titulo');
const elementoA = document.querySelector("a");
const elementoUL = document.querySelector("ul");
const elementoOL = document.getElementById('lista-ordenada');
elementoUL.innerHTML = `
    <li>Item 01</li>
    <li>Item 02</li>
    <li>Item 03</li>
`

elementoH1.innerText = ("Teste de título para projeto 2");
elementoA.innerText = ("Link PROZ");

elementoOL.innerHTML = `
    <li><a href="https://www.google.com.br" target="_blank">Google</a></li>
    <li><a href="https://www.globo.com" target="_blank">Globo</a></li>
    <li><a href="https://www.band.uol.com.br" target="_blank">Band</a></li>
`
