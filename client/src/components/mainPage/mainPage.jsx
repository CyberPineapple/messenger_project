import React from "react";
import style from "./mainPage.module.css";
import { Animated } from "react-animated-css";
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

class MainPage extends React.Component{

  render(){
    return (
      <Animated animationIn="zoomIn"animationInDuration={1000} isVisible={true}>
        <div className={style.layout}>
        <div className={style.menu}>
          <div className={style.menu_image}></div>
          <p>{this.props.login}</p>
        </div>
        <div className={style.chatbox}>
          <div className={style.output}>

          </div>
          <div className={style.input}>
            <textarea></textarea>
            <div className={style.button}>Отправить</div>
          </div>
        </div>
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

const mapDispatchToProps = dispatch => {
}

export default connect(mapStateToProps, mapDispatchToProps)(MainPage);