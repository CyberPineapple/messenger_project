
export const setPage = value => {
    return{
        type: 'SET_PAGE',
        page: value
    }
}

export const setLogin = value => {
    return{
        type: 'SET_LOGIN',
        login: value
    }
}

export const setPassword = value => {
    return{
        type: 'SET_PASSWORD',
        password: value
    }
}

export const removeLogin = () => {
    return{
        type: 'REMOVE_LOGIN'
    }
}

export const removePassword = () => {
    return{
        type: 'REMOVE_PASSWORD',
    }
}

export const authentification = value => {
    return {
        type: 'AUTHENTIFICATION',
        authentification: value
    }
}


export const connect = value => {
    return {
        type: 'CONNECT',
        connect: value
    }
}

export const setMessage = value => {
    return{
        type: 'SET_MESSAGE',
        message: value
    }
}

export const setMessagesList = value => {
    return{
        type: 'SET_MESSAGES_LIST',
        messagesList: value
    }
}

export const removeMessagesList = () => {
    return{
        type: 'REMOVE_MESSAGES_LIST',
    }
}

export const removeMessage = () => {
    return{
        type: 'REMOVE_MESSAGE'
    }
}

export const setChatList = value => {
    return{
        type: 'SET_CHAT_LIST',
        chatList: value
    }
}

export const addChatName = value => {
    return{
        type: 'ADD_CHAT_NAME',
        chatName: value
    }
}

export const removeChatName = () => {
    return{
        type: 'REMOVE_CHAT_NAME',
    }
}

export const addChatPassword = value => {
    return{
        type: 'ADD_CHAT_PASSWORD',
        chatPassword: value
    }
}

export const removeChatPassword = () => {
    return{
        type: 'REMOVE_CHAT_PASSWORD',
    }
}

export const activeChat = value => {
    return {
        type: 'ACTIVE_CHAT',
        chat: value
    }
}

export const renderChatOutput = (value) =>{
    return {
        type: 'RENDER_CHAT_OUTPUT',
        payload: value
    }
}

export const earlierMessagesList = (value) =>{
    return {
        type: 'EARLIER_MESSAGES',
        payload: value
    }
}

export const addImage = value => {
    return {
        type: 'ADD_IMAGE',
        image: value
    }
}

export const clearImages = () => {
    return {
        type: 'CLEAR_IMAGES'
    }
}
.