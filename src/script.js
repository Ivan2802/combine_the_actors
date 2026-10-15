artist_1 = document.querySelector(".a1")
artists_block = document.querySelector(".artists_list")
button = document.querySelector(".btn")
btn_add = document.querySelector(".btn_add")
result = document.querySelector(".result")

FEILDS_COUNTER = 2
const SERVER = "http://127.0.0.1:8000/"
// const SERVER = "https://combine-the-actors.de2.netrun.io/"

function make_request() {
    data_artist = {
        "artists": []
    }
    all_artists_inputs = [...artists_block.children]
    all_artists_inputs.forEach(child => {
        data_artist["artists"].push(child.value)
    });
    console.log(JSON.stringify(data_artist))
    fetch(SERVER + `get_artist`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data_artist)
    })
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

function add_field_for_name() {
    new_field = document.createElement("input")
    new_field.setAttribute("type", "text")
    new_field.classList.add(`a${FEILDS_COUNTER}`)
    FEILDS_COUNTER += 1
    artists_block.appendChild(new_field)
}


button.addEventListener("click", make_request)
btn_add.addEventListener("click", add_field_for_name)