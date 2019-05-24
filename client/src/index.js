import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { Provider } from "react-redux";
import { store } from './store/configureStore'
import { socket } from './websockets/websocket'
import { setPage, connect, setMessagesList, setChatList, renderChatOutput, earlierMessagesList, activeChat } from './actions/actions';

socket.onopen = () =>{
  store.dispatch(setPage('authentification'));
  store.dispatch(connect(true));
}


socket.onclose = () =>{
  console.log('disconnect');
  store.dispatch(setPage('loading'));
}

socket.onmessage = (response) =>{
  let data = JSON.parse(response.data);
  console.log(data);
  if (data !== null){
    switch (data.Type){
      case 'login': {
        if (data.Status === 'success'){
          store.dispatch(setPage('main'));
          store.dispatch(activeChat('general'));
          let data = {
            Type: 'chat',
            Command: 'choice',
            Chat: 'general'
          }
          data = JSON.stringify(data);
          socket.send(data);
        } else if (data.Status === 'error'){
          console.log('Ошибка авторизации');
        }
        break;
      }
      case 'registration': {
        console.log('Регистрация');
        break;
      }
      case 'chat': {
        if (data.Command === 'list'){
          store.dispatch(setChatList(data.Chats));
        };
        if (data.Command === 'choice'){
          store.dispatch(setMessagesList(data.Messages));
          store.dispatch(renderChatOutput(true));
        }
        if (data.Command === 'message'){
          store.dispatch(setMessagesList(data.Message));
        }
        if (data.Command === 'earlier'){
          store.dispatch(earlierMessagesList(data.Messages));
        }
        break;
      }
      default: {
        console.log(data);
        break;
      }
    }
  }
}

socket.onerror= (error) => {
  console.log("error: ", error);
}

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);