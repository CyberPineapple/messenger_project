import React from "react";
import style from "./mainPage.module.css";
import { Animated } from "react-animated-css";
import Chatbox from "../chatbox/chatbox";
import Menu from "../menu/menu";

export default class MainPage extends React.Component{

  render(){
    return (
      <Animated animationIn="fadeIn"animationInDuration={1000} isVisible={true}>
        <div className={style.layout}>
          <Menu />
          <Chatbox />
        </div>
      </Animated>
    )
  }
}