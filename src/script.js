artist_1 = document.querySelector(".a1")
artist_2 = document.querySelector(".a2")
button = document.querySelector(".btn")
btn_add = document.querySelector(".btn_add")
result = document.querySelector(".result")

// const SERVER = "http://127.0.0.1:8000/"
const SERVER = "https://combine-the-actors.de2.netrun.io/"

function make_request() {
    console.log(`get_artist/${artist_1.value}/${artist_2.value}`)
    fetch(SERVER + `get_artist/${artist_1.value}/${artist_2.value}`) // remake path r
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        fill_result(data)
    })
}

function fill_result(data) {
    result.innerHTML = '<h3>Here are their films together</h3>'
    data.forEach(el => {
        result.innerHTML += `${el}<br>`
    })
}

function add_actor() {

}


button.addEventListener("click", make_request)
btn_add.addEventListener("click", add_actor)