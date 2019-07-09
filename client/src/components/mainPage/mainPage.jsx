import React from "react";
import style from "./MainPage.module.css";
import { Animated } from "react-animated-css";
import Chatbox from "../Chatbox/Chatbox"
import Menu from "../Menu/Menu";

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