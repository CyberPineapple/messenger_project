import { createStore } from 'redux';
import { rootReducer } from '../reducers/rootReducer';
import { initialState } from './initialState';

 export const store = createStore(rootReducer, initialState);