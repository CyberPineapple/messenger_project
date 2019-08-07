export const setPage = value => {
  return {
    type: "SET_PAGE",
    payload: value
  };
};

export const setLoginAction = value => {
  return {
    type: "SET_LOGIN",
    payload: value
  };
};

export const setPasswordAction = value => {
  return {
    type: "SET_PASSWORD",
    payload: value
  };
};

export const setMessage = value => {
  return {
    type: "SET_MESSAGE",
    payload: value
  };
};

export const setMessagesList = value => {
  return {
    type: "SET_MESSAGES_LIST",
    payload: value
  };
};

export const removeMessagesList = () => {
  return {
    type: "REMOVE_MESSAGES_LIST"
  };
};

export const removeMessage = () => {
  return {
    type: "REMOVE_MESSAGE"
  };
};

export const setChatList = value => {
  return {
    type: "SET_CHAT_LIST",
    payload: value
  };
};

export const addChatName = value => {
  return {
    type: "ADD_CHAT_NAME",
    payload: value
  };
};

export const removeChatName = () => {
  return {
    type: "REMOVE_CHAT_NAME"
  };
};

export const addChatPassword = value => {
  return {
    type: "ADD_CHAT_PASSWORD",
    payload: value
  };
};

export const removeChatPassword = () => {
  return {
    type: "REMOVE_CHAT_PASSWORD"
  };
};

export const activeChat = value => {
  return {
    type: "ACTIVE_CHAT",
    payload: value
  };
};

export const renderChatOutput = value => {
  return {
    type: "RENDER_CHAT_OUTPUT",
    payload: value
  };
};

export const earlierMessagesList = value => {
  return {
    type: "EARLIER_MESSAGES",
    payload: value
  };
};

export const setImageAction = value => {
  return {
    type: "SET_IMAGE",
    payload: value
  };
};

export const setOnlineUsers = value => {
  return {
    type: "SET_ONLINE_USERS",
    payload: value
  };
};

export const replyAction = value => ({
  type: 'REPLY_MESSAGE',
  payload: value
})
