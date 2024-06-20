
function consult_user() {
    let id_user = document.getElementById("ident").value
    let obj_user = {
        "id": id_user,
        "passw": "12345" // Es solo para pruebas no se utiliza
    }
    fetch("/consult_user", {
        "method":"post",
        "headers":{"Content-Type":"application/json"},
        "body":JSON.stringify(obj_user)
    })
    .then(resp => resp.json())
    .then(data => {
        alert(data)
    })
    .catch(err => {
        alert("Error " + err)
    })
}