// const app = document.querySelector("#app");
//
// app.addEventListener(() => {
//     const ws = new WebSocket("ws://localhost:8765");
//     ws.onmessage = ({ data }) => {
//         const content = document.createTextNode(data);
//         app.appendChild(content);
//     }
// });
window.addEventListener("DOMContentLoaded", () => {
    const messages = document.createElement("ul");
    document.body.appendChild(messages);

    const websocket = new WebSocket("ws://localhost:8765/");
    websocket.onmessage = ({ data }) => {
        const message = document.createElement("li");
        const content = document.createTextNode(data);
        message.appendChild(content);
        messages.appendChild(message);
    };
});
