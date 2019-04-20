import { createStore } from 'redux';
import { rootReducer, initialState } from '../reducers/rootReducer';

 export const store = createStore(rootReducer, initialState);