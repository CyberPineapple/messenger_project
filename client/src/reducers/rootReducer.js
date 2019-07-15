import { initialState } from '../store/initialState';

export function rootReducer(state = initialState, action){
    switch (action.type){
        case 'SET_PAGE': return {...state, page: action.payload};
        case 'SET_LOGIN': return {...state, login: action.payload};
        case 'SET_PASSWORD': return {...state, password: action.payload};
        case 'REMOVE_LOGIN': return {...state, login: ''};
        case 'REMOVE_PASSWORD': return {...state, password: ''};
        case 'AUTHENTIFICATION': return {...state, authentification: action.payload};
        case 'CONNECT': return {...state, connect: action.payload};
        case 'SET_MESSAGE': return {...state, message: action.payload};
        case 'SET_MESSAGES_LIST': return {...state, messagesList: state.messagesList.concat(action.payload)};
        case 'REMOVE_MESSAGE': return {...state, message: ''};
        case 'SET_CHAT_LIST': return {...state, chatList: action.payload};
        case 'ADD_CHAT_NAME': return {...state, chatName: action.payload};
        case 'REMOVE_CHAT_NAME': return {...state, chatName: ''};
        case 'ADD_CHAT_PASSWORD': return {...state, chatPassword: action.payload};
        case 'REMOVE_CHAT_PASSWORD': return {...state, chatPassword: ''};
        case 'ACTIVE_CHAT': return {...state, activeChat: action.payload};
        case 'REMOVE_MESSAGES_LIST': return{...state, messagesList: []};
        case 'RENDER_CHAT_OUTPUT': return{...state, renderChatOutput: action.payload};
        case 'EARLIER_MESSAGES': return{...state, messagesList: [...action.payload, ...state.messagesList]};
        case 'SET_IMAGE': return {...state, image: action.payload};
        default: return state;
    }
}
