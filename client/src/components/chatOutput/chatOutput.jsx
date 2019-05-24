import React from "react";
import { connect } from "react-redux";
import style from "./chatOutput.module.css";
import { socket } from "../../websockets/websocket";

class ChatOutput extends React.Component {
  render() {
    const { messagesList } = this.props;
    let messages = [];
    console.log(this.props.messagesList);
    if (messagesList.length !== 0) {
      messages = messagesList.map((value, id) => (
        <div key={id} className={style.message}>
          <div className={style.message_user}>{value.user}</div>
          <div className={style.message_text}>{value.text}</div>
          <div className={style.message_time}>{value.date}</div>
        </div>
      ));
    }
    return (
      <div className={style.output}>
        <div className={style.nameChat}>{this.props.activeChat}</div>
        <div className={style.messagesList} onScroll={e => this.scrollChat(e)}>{messages}</div>
      </div>
    );
  }

  componentDidMount() {
    let el = document.querySelector("." + style.messagesList);
    el.scrollTop = el.scrollHeight;
  }

  scrollChat = value => {
    if (value.target.scrollTop === 0) {
      let data = {
        Type: "chat",
        Command: "earlier"
      };
      socket.send(JSON.stringify(data));
      value.target.scrollTop = 10;
    }
  };
}

const mapStateToProps = store => {
  return {
    messagesList: store.messagesList,
    activeChat: store.activeChat
  };
};

export default connect(
  mapStateToProps,
  null
)(ChatOutput);
