import { initialState } from "../store/initialState";

export function rootReducer(state = initialState, action) {
  const { type, payload } = action;
  switch (type) {
    case "SET_PAGE":
      return { ...state, page: payload };
    case "SET_LOGIN":
      return {
        ...state,
        user: {
          login: payload,
          password: state.user.password
        }
      };
    case "SET_PASSWORD":
      return {
        ...state,
        user: {
          login: state.user.login,
          password: payload
        }
      };
    case "SET_ONLINE_USERS": {
      return { ...state, usersOnline: payload };
    }
    case "SET_MESSAGE":
      return { ...state, message: payload };
    case "SET_MESSAGES_LIST":
      return {
        ...state,
        messagesList: state.messagesList.concat(payload)
      };
    case "REMOVE_MESSAGE":
      return { ...state, message: "" };
    case "SET_CHAT_LIST":
      return { ...state, chatList: payload };
    case "ADD_CHAT_NAME":
      return { ...state, chatName: payload };
    case "REMOVE_CHAT_NAME":
      return { ...state, chatName: "" };
    case "ADD_CHAT_PASSWORD":
      return { ...state, chatPassword: payload };
    case "REMOVE_CHAT_PASSWORD":
      return { ...state, chatPassword: "" };
    case "ACTIVE_CHAT":
      return { ...state, activeChat: payload };
    case "REMOVE_MESSAGES_LIST":
      return { ...state, messagesList: [] };
    case "RENDER_CHAT_OUTPUT":
      return { ...state, renderChatOutput: payload };
    case "EARLIER_MESSAGES":
      return {
        ...state,
        messagesList: [...payload, ...state.messagesList]
      };
    case "SET_IMAGE":
      return { ...state, image: payload };
    case "REPLY_MESSAGE":
      return { ...state, replyMessage: payload };
    default:
      return state;
  }
}
