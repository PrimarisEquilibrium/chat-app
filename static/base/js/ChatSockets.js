const username = JSON.parse(document.getElementById("username").textContent)

document.querySelector("#submit").onclick = function (e) {
    e.preventDefault()
    const messageInputDom = document.querySelector(".input-box")
    if (messageInputDom.value !== ""){
        const message = messageInputDom.value
        chatSocket.send(JSON.stringify({
            "message": message,
            "username": username
        }))
        messageInputDom.value = ""
    }
}

const chatSocket = new WebSocket(
    `ws://${window.location.host}/ws/chat`
)

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data)

    chatArea = document.querySelector(".chat-area")

    newDiv = document.createElement("div")
    newDiv.setAttribute("class", "chat-item")
    chatArea.append(newDiv)

    innerDiv = document.createElement("div")
    innerDiv.setAttribute("class", "chat-text")
    innerDiv.innerText = `${data.username}: ${data.message}`
    newDiv.append(innerDiv)

}