import React from "react";
import style from "./MainPage.module.css";
import ChatContainer from "./ChatContainer/ChatContainer";
import MainMenu from "./MainMenu";

export default class MainPage extends React.Component {
  render() {
    return (
      <div className={style.layout}>
        <MainMenu />
        <ChatContainer />
      </div>
    );
  }
}
