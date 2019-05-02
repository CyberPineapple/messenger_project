
export const initialState = {
    page: 'loading',
    login: 'login',
    password: 'password',
    authentification: false,
    connect: false,
    message: '',
    messagesList: [],
    chatList: [],
    chatName: '',
    activeChat: ''
}

export function rootReducer(state = initialState, action){
    switch (action.type){
        case 'SET_PAGE': return {...state, page: action.page};
        case 'SET_LOGIN': return {...state, login: action.login};
        case 'SET_PASSWORD': return {...state, password: action.password};
        case 'REMOVE_LOGIN': return {...state, login: ''};
        case 'REMOVE_PASSWORD': return {...state, password: ''};
        case 'AUTHENTIFICATION': return {...state, authentification: action.authentification};
        case 'CONNECT': return {...state, connect: action.connect};
        case 'SET_MESSAGE': return {...state, message: action.message};
        case 'SET_MESSAGES_LIST': return {...state, messagesList: state.messagesList.concat(action.messagesList)};
        case 'REMOVE_MESSAGE': return {...state, message: ''};
        case 'SET_CHAT_LIST': return {...state, chatList: action.chatList};
        case 'ADD_CHAT_NAME': return {...state, chatName: action.chatName};
        case 'REMOVE_CHAT_NAME': return {...state, chatName: ''};
        case 'ACTIVE_CHAT': return {...state, activeChat: action.chat};
        case 'REMOVE_MESSAGES_LIST': return{...state, messagesList: []};
        default: return state;
    }
}
