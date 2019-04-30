import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { Provider } from "react-redux";
import { store } from './store/configureStore'
import { socket } from './websockets/websocket'
import { setPage, connect, setMessagesList } from './actions/actions';


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
    case 'message': {
      if (data.Status === 'success'){
        store.dispatch(setMessagesList(data.Text))
      }
      break;
    }
    default: {
      console.log(data);
      break;
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
