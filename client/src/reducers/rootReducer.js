
export const initialState = {
    page: 'loading',
    login: 'login',
    password: 'password',
    connect: false,
}

export function rootReducer(state = initialState, action){
    switch (action.type){
        case 'SET_PAGE': return {...state, page: action.page};
        case 'SET_LOGIN': return {...state, login: action.login};
        case 'SET_PASSWORD': return {...state, password: action.password};
        case 'REMOVE_LOGIN': return {...state, login: ''};
        case 'REMOVE_PASSWORD': return {...state, password: ''};
        default: return state;
    }
}
