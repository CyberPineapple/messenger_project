import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { Provider } from "react-redux";
import { store } from './store/configureStore'
import { socket } from './websockets/websocket'
import { setPage } from './actions/actions';

socket.onopen = () =>{
  store.dispatch(setPage('authentification'));
}

socket.onclose = () =>{
  console.log('disconnect');
  store.dispatch(setPage('loading'));
}

socket.onmessage = (data) =>{
  console.log(data.data);
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
