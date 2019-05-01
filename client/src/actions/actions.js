
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
        type: 'REMOVE_LOGIN',
    }
}

export const removePassword = value => {
    return{
        type: 'SET_PASSWORD',
        password: ''
    }
}