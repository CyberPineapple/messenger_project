import React from "react";
import style from "./MainPage.module.css";
import Chatbox from "./Chatbox/Chatbox";
import MainMenu from "./MainMenu";

export default class MainPage extends React.Component {
  render() {
    return (
      <div className={style.layout}>
        <MainMenu />
        <Chatbox />
      </div>
    );
  }
}
