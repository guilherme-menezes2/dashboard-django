const keyApi = "bc08edb0630c57710bc33d08b882d7a7"

padrao();

function dadosNaTela(dados){
    document.querySelector(".box__titulo").innerHTML = dados.name;
    document.querySelector(".info__temp").innerHTML = Math.round(dados.main.temp) + "°C";
    document.querySelector(".info__condicao").innerHTML = dados.weather[0].description;
    document.querySelector(".info__umid").innerHTML = "Umidade: " + dados.main.humidity + "%"
    document.querySelector(".info__img").src = `http://openweathermap.org/img/wn/${dados.weather[0].icon}@2x.png`
}

async function buscarCidade(cidade){
    const dados = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${cidade}&appid=${keyApi}&lang=pt_br&units=metric`).then( response => response.json());
    dadosNaTela(dados);
}

function buttonClick(){
    const cidade = document.querySelector(".box__search").value;
    buscarCidade(cidade);
}

function padrao(){
    const cidade = "Pedreiras"
    buscarCidade(cidade);
}