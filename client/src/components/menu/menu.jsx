import React from "react";
import { connect } from "react-redux";
import style from "./menu.module.css";
import { socket } from "../../websockets/websocket";
import { bindActionCreators } from "redux";
import { addChatName, removeChatName, activeChat, removeMessagesList } from "../../actions/actions";

class Menu extends React.Component {
  render() {
    let chats = this.props.chatList;
    chats = chats.map((value, id) => (
      <div key={id} onClick={()=>this.choiceChat(value)} className={style.menu_chat_list_item}>{value}</div>
    ))
    return (
      <div className={style.menu}>
        <div className={style.menu_image} />
        <p className={style.menu_login}>{this.props.login}</p>
        <p className={style.menu_chat}>Создать чат</p>
        <input
          type="text"
          className={style.input}
          onChange={e => this.props.addChatName(e.target.value)}
          onKeyPress={e => this.sendChat(e)}
          value={this.props.chatName}
          onClick={()=> this.props.removeChatName()}
          maxLength={12}
        />
        <p className={style.menu_chat}>Список чатов:</p>
        <div className={style.menu_chat_list}>
          {chats}
        </div>
      </div>
    );
  }

  sendChat = e => {
    if (this.props.chatName !== "") {
      if (e.key === "Enter") {
        let data = {
          Type: "chat",
          Command: "create",
          User: this.props.login,
          Chat: this.props.chatName
        };
        data = JSON.stringify(data);
        socket.send(data);
        this.props.removeChatName();
      }
    }
  };

  choiceChat = (name) =>{
    this.props.activeChat(name);
    let data = {
      Type: 'chat',
      Command: 'choice',
      Chat: name
    }
    data = JSON.stringify(data);
    socket.send(data);
    this.props.removeMessagesList();
  }
}

const mapStateToProps = store => {
  return {
    login: store.login,
    chatList: store.chatList,
    chatName: store.chatName,
    store: store
  };
};

const mapDispatchToProps = dispatch => {
  return bindActionCreators(
    { addChatName: addChatName, removeChatName: removeChatName, activeChat: activeChat, removeMessagesList: removeMessagesList },
    dispatch
  );
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Menu);
