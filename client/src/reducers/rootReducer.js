import { setPage } from "../actions/actions";
import { connect } from 'react-redux';
import { bindActionCreators } from "redux";


export const initialState = {
    page: 'authentification',
    login: '',
    password: ''
}

export function rootReducer(state = initialState, action){
    switch (action.type){
        case 'SET_PAGE': return {...state, page: action.page};
        case 'SET_LOGIN': return {...state, login: action.login};
        case 'SET_PASSWORD': return {...state, password: action.password};
        case 'REMOVE_LOGIN': return {...state, login: ''};
        case 'REMOVE_PASSWORD': return {...state, password: action.password};
        default: return state;
    }
}



let socket = new WebSocket("ws://localhost:8080/ws");

socket.onopen = () =>{
  console.log('connect');
  socket.send("hentai");
}

socket.onclose = () =>{
  console.log('disconnect');
}




socket.onmessage = (data, props) =>{
  console.log(data);
  this.props.setPage('main')
}

const mapDispatchToProps = dispatch => {
    return bindActionCreators({setPage: setPage}, dispatch);
}

connect(mapDispatchToProps);