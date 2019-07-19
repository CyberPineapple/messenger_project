import { store } from "../store/configureStore";
import {
  setPage,
  setMessagesList,
  setChatList,
  renderChatOutput,
  earlierMessagesList,
  activeChat,
  setOnlineUsers
} from "../actions/actions";
import sound from "../audio/new_message.mp3";

export const socket = new WebSocket(
  "wss://host-94-103-84-32.hosted-by-vdsina.ru:443/"
);

socket.onopen = () => {
  store.dispatch(setPage("authentification"));
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
      case "account": {
        if (data.Status === "success") {
          store.dispatch(setPage("main"));
          let data = {
            Type: "chat",
            Command: "choice",
            Chat: "general"
          };
          data = JSON.stringify(data);
          sendMessage(data);
          data = {
            Type: "chat",
            Command: "connected"
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
          if (data.Message.user !== store.getState().user.login) {
            const audio = new Audio();
            audio.src = sound;
            audio.play();
          }
          store.dispatch(setMessagesList(data.Message));
        }
        if (data.Command === "earlier") {
          if (data.Messages.length !== 0) {
            store.dispatch(earlierMessagesList(data.Messages));
          }
        }
        if (data.Command === 'connected'){
          store.dispatch(setOnlineUsers(data.Online))
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

const sendMessage = data => {
  console.log(data)
  socket.send(data);
};

export default sendMessage;
