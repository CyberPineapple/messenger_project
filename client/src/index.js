import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { Provider } from "react-redux";
import { store } from './store/configureStore'
import { socket } from './websockets/websocket'
import { setPage, connect, setMessagesList, setChatList } from './actions/actions';

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
        }
        if (data.Command === 'message'){
          store.dispatch(setMessagesList(data.Message));  
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