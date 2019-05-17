import React from "react";
import { connect } from "react-redux";
import style from "./chatbox.module.css";
import { bindActionCreators } from "redux";
import { setMessage, removeMessage } from "../../actions/actions.js";
import { socket } from "../../websockets/websocket";
import ChatOutput from '../chatOutput/chatOutput';

class Chatbox extends React.Component {
  render() {
    let chat = null;
    console.log(this.props.renderChatOutput);
    if (this.props.renderChatOutput){
      chat = <ChatOutput />
    } else {
      chat = null;
    }
    console.log(chat);
    return (
      <div className={style.block}>
        <div className={style.chat}>
          {chat}
        </div>
        <div className={style.input}>
          <textarea
            onChange={event => this.onChangeMessage(event.target.value)}
            value={this.props.message}
            onKeyPress={e => this.pressEnter(e)}
          />
          <div className={style.button} onClick={() => this.sendMessage()}>
            Отправить
          </div>
        </div>
      </div>
    );
  }

  sendMessage = () => {
    if (this.props.message !== "" && this.props.activeChat !== "") {
      let data = {
        Type: "chat",
        Command: "message",
        Text: this.props.message
      };
      data = JSON.stringify(data);
      socket.send(data);
      this.props.removeMessage();
    }
  };

  pressEnter = e => {
    if (e.key === "Enter") {
      this.sendMessage();
    }
  };

  onChangeMessage = value => {
    if (value !== "\n") this.props.setMessage(value);
  };
}

const mapStateToProps = store => {
  return {
    message: store.message,
    login: store.login,
    activeChat: store.activeChat,
    renderChatOutput: store.renderChatOutput
  };
};

const mapDispatchToProps = dispatch => {
  return bindActionCreators(
    { setMessage: setMessage, removeMessage: removeMessage },
    dispatch
  );
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Chatbox);
