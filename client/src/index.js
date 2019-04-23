import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { Provider } from "react-redux";
import { store } from './store/configureStore'
import { socket } from './websockets/websocket'
import { setLogin } from './actions/actions';

socket.onopen = () =>{
  console.log('connect');
  let data = {
    Type: "reg",
    Login: "login",
    Password: "password"
  }
  data = JSON.stringify(data);
  socket.send(data);
}

store.dispatch(setLogin("hello"));

socket.onclose = () =>{
  console.log('disconnect');
}

socket.onmessage = (data) =>{
  console.log(data.data);
}


ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);
