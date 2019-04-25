import React from "react";
import style from "./mainPage.module.css";
import { Animated } from "react-animated-css";
import { connect } from 'react-redux';
import Chatbox from "../chatbox/chatbox";

class MainPage extends React.Component{

  render(){
    return (
      <Animated animationIn="zoomIn"animationInDuration={1000} isVisible={true}>
        <div className={style.layout}>
          <div className={style.menu}>
            <div className={style.menu_image}></div>
            <p>{this.props.login}</p>
          </div>
          <Chatbox />
        </div>
      </Animated>
    )
  }
}

const mapStateToProps = store => {
  return {
    login: store.login
  }
}



export default connect(mapStateToProps)(MainPage);