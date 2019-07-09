import { store } from "../store/configureStore";
import {
  setPage,
  connect,
  setMessagesList,
  setChatList,
  renderChatOutput,
  earlierMessagesList,
  activeChat
} from "../actions/actions";
import sound from "../audio/new_message.mp3";

export const socket = new WebSocket(
  "wss://host-94-103-84-32.hosted-by-vdsina.ru:443/"
);

socket.onopen = () => {
  store.dispatch(setPage("authentification"));
  store.dispatch(connect(true));
};

socket.onclose = () => {
  console.log("disconnect");
  store.dispatch(setPage("loading"));
};

socket.onmessage = response => {
  let data = JSON.parse(response.data);
  console.log(data);
  if (data !== null) {
    switch (data.Type) {
      case "login": {
        if (data.Status === "success") {
          store.dispatch(setPage("main"));
          let data = {
            Type: 'chat',
            Command: 'connected'
          };
          data = JSON.stringify(data);
          sendMessage(data);
          store.dispatch(renderChatOutput(false));
        } else if (data.Status === "error") {
          console.log("Ошибка авторизации");
        }
        break;
      }
      case "registration": {
        console.log("Регистрация");
        break;
      }
      case "chat": {
        if (data.Command === "list") {
          store.dispatch(setChatList(data.Chats));
        }
        if (data.Command === "choice") {
          store.dispatch(activeChat(data.Chat));
          store.dispatch(setMessagesList(data.Messages));
          store.dispatch(renderChatOutput(true));
        }
        if (data.Command === "message") {
          store.dispatch(setMessagesList(data.Message));
          const audio = new Audio();
          audio.src = sound;
          audio.play();
        }
        if (data.Command === "earlier") {
          if (data.Messages.length !== 0) {
            store.dispatch(earlierMessagesList(data.Messages));
          }
        }
        break;
      }
      default: {
        console.log(data);
        break;
      }
    }
  }
};

socket.onerror = error => {
  console.log("error: ", error);
};

const sendMessage = (data) => {
  socket.send(data);
}

export default sendMessage;
