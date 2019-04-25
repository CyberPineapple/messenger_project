
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

export const authentification = (value) => {
    return {
        type: 'AUTHENTIFICATION',
        authentification: value
    }
}


export const connect = (value) => {
    return {
        type: 'CONNECT',
        connect: value
    }
}