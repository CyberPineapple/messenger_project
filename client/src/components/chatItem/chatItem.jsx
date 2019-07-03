import React from "react";
import { connect } from "react-redux";
import style from "./chatItem.module.css";
import { bindActionCreators } from "redux";
import {
  removeMessagesList,
  activeChat,
  renderChatOutput
} from "../../actions/actions";
import { socket } from "../../websockets/websocket";

class ChatItem extends React.Component {
  constructor() {
    super();
    this.state = {
      viewPasswordField: false,
      chatPassword: ""
    };
  }

  render() {
    let chat;
    const { value } = this.props;
    if (value.Closed === false) {
      chat = (
        <div
          onClick={this.choiceChat}
          className={style.menu_chat_list_item}
        >
          <p>{value.Chat}</p>
        </div>
      );
    } else if (value.Closed === true) {
      let passwordField = "";
      if (this.state.viewPasswordField === true) {
        passwordField = (
          <input
            type="text"
            value={this.props.chatPassword}
            onChange={e => this.onChangePassword(e.target.value)}
            onKeyPress={e => this.onPressEnter(e)}
            maxLength={30}
            autoFocus
          />
        );
      }
      chat = (
        <div
          className={style.menu_chat_list_item}
          onClick={() =>
            this.setState({
              viewPasswordField: true
            })
          }
          onMouseLeave={() =>
            this.setState({
              viewPasswordField: false
            })
          }
        >
          <p>{value.Chat}</p>
          {passwordField}
        </div>
      );
    }
    return <React.Fragment>{chat}</React.Fragment>;
  }

  choiceChat = () => {
    const chatName = this.props.value.Chat;
    this.props.activeChat(chatName);
    let data = {
      Type: "chat",
      Command: "choice",
      Chat: chatName
    };
    data = JSON.stringify(data);
    this.props.renderChatOutput(false);
    this.props.removeMessagesList();
    socket.send(data);
  };

  onPressEnter = e => {
    if (e.key === "Enter") {
      this.choiceSecretChat(this.props.value.Chat);
    }
  };

  choiceSecretChat = name => {
    this.props.activeChat(name);
    let data = {
      Type: "chat",
      Command: "choice",
      Chat: name,
      Password: this.state.chatPassword
    };
    data = JSON.stringify(data);
    socket.send(data);
    this.props.renderChatOutput(false);
    this.props.removeMessagesList();
    this.setState({
      viewPasswordField: false,
      chatPassword: ""
    });
  };

  onChangePassword = value => {
    this.setState({
      chatPassword: value
    });
  };
}

const mapDispatchToProps = dispatch => {
  return bindActionCreators(
    {
      removeMessagesList: removeMessagesList,
      activeChat: activeChat,
      renderChatOutput: renderChatOutput
    },
    dispatch
  );
};

export default connect(
  null,
  mapDispatchToProps
)(ChatItem);
