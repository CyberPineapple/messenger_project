import React from "react";
import { connect } from "react-redux";
import styles from "./MainMenu.module.css";
import { socket } from "../../../websockets/websocket";
import { bindActionCreators } from "redux";
import {
  addChatName,
  removeChatName,
  activeChat,
  removeMessagesList,
  addChatPassword,
  removeChatPassword
} from "../../../actions/actions";
import ChatItem from "./ChatItem/ChatItem";
import Clock from "./Clock/Clock";

class MainMenu extends React.Component {
  state = {
    isView: false,
    viewChatInput: false
  };

  clickButton = () => {
    const { isView } = this.state;
    this.setState({
      isView: !isView
    });
  };
  render() {
    const { isView } = this.state;
    console.log(isView);
    let chats = this.props.chatList;
    chats = chats.map((value, id) => <ChatItem value={value} key={id} />);
    let chatInput = "";
    if (this.state.viewChatInput === false) {
      chatInput = (
        <p
          className={styles.menu_chat}
          onClick={() =>
            this.setState({ viewChatInput: !this.state.viewChatInput })
          }
        >
          Создать чат
        </p>
      );
    } else if (this.state.viewChatInput === true) {
      chatInput = (
        <React.Fragment>
          <p
            className={styles.menu_chat}
            onClick={() =>
              this.setState({ viewChatInput: !this.state.viewChatInput })
            }
          >
            Закрыть
          </p>
          <p className={styles.menu_chat}>Название чата</p>
          <input
            type="text"
            className={styles.input}
            onChange={e => this.props.addChatName(e.target.value)}
            onKeyPress={e => this.sendChat(e)}
            value={this.props.chatName}
            onClick={() => this.props.removeChatName()}
            maxLength={12}
          />
          <p className={styles.menu_chat}>Пароль (не обязательно)</p>
          <input
            type="text"
            className={styles.input}
            onChange={e => this.props.addChatPassword(e.target.value)}
            onKeyPress={e => this.sendChat(e)}
            value={this.props.chatPassword}
            onClick={() => this.props.removeChatPassword()}
            maxLength={30}
          />
        </React.Fragment>
      );
    }

    return (
      <React.Fragment>
        <div className={isView ? styles.blockView : styles.blockHide}>
          <button className={styles.button} onClick={this.clickButton}>
            <div className={styles.burger}>
              <div className={isView ? styles.line1Active : styles.line1} />
              <div className={isView ? styles.line2Active : styles.line2} />
              <div className={isView ? styles.line3Active : styles.line3} />
            </div>
          </button>
          <div className={styles.menu}>
            <div className={styles.menu_image} />
            <p className={styles.menu_login}>{this.props.login}</p>
            {chatInput}
            <p className={styles.menu_chat}>Список чатов:</p>
            <div className={styles.menu_chat_list}>{chats}</div>
            <Clock />
          </div>
        </div>
      </React.Fragment>
    );
  }

  sendChat = e => {
    if (this.props.chatName !== "") {
      if (e.key === "Enter") {
        let data = {
          Type: "chat",
          Command: "create",
          Chat: this.props.chatName
        };
        if (this.props.chatPassword !== "") {
          data["Password"] = this.props.chatPassword;
        }
        data = JSON.stringify(data);
        socket.send(data);
        this.props.removeChatName();
        this.props.removeChatPassword();
      }
    }
  };
}

const mapStateToProps = store => {
  return {
    login: store.login,
    chatList: store.chatList,
    chatName: store.chatName,
    chatPassword: store.chatPassword
  };
};

const mapDispatchToProps = dispatch => {
  return bindActionCreators(
    {
      addChatName: addChatName,
      removeChatName: removeChatName,
      activeChat: activeChat,
      removeMessagesList: removeMessagesList,
      removeChatPassword: removeChatPassword,
      addChatPassword: addChatPassword
    },
    dispatch
  );
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(MainMenu);
