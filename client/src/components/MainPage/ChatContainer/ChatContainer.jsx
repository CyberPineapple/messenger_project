import React from "react";
import style from "./ChatContainer.module.css";
import ChatOutput from "./ChatOutput/ChatOutput";
import ChatInput from "./ChatInput/ChatInput";

export default class ChatContainer extends React.Component {
  render() {
    return (
      <div className={style.block}>
        <ChatOutput />
        <ChatInput />
      </div>
    );
  };
};
