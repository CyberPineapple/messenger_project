import React from "react";
import style from "./ChatContainer.module.css";
import ChatOutputContainer from "../../../containers/ChatOutputContainer";
import ChatInputContainer from "../../../containers/ChatInputContainer";

export default class ChatContainer extends React.Component {
  render() {
    return (
      <div className={style.block}>
        <ChatOutputContainer />
        <ChatInputContainer />
      </div>
    );
  };
};
