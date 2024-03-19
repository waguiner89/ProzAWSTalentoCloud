// let elementoH1 = document.querySelector("h1");
let elementoMain = document.querySelector("main");

// elementoH1.innerText = "Novo título JS";
elementoMain.innerHTML = `
    <h2>Novo subtítulo</h2>
    <ul>
        <li>Elemento de lista JS 01</li>
        <li>Elemento de lista JS 02</li>
        <li>Elemento de lista JS 03</li>
    </ul>
`

// console.log(elementoH1);
// console.log(elementoH1.innerText);
// console.log(elementoMain);
// console.log(elementoMain.innerText);
console.log(elementoMain.innerHTML);