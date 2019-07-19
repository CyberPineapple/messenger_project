import React from "react";
import { connect } from "react-redux";
import style from "./ChatOutput.module.css";
import sendMessage from "../../../../websockets/websocket";
import Message from "./Message/Message";

class ChatOutput extends React.Component {
  render() {
    const { messagesList } = this.props;
    let messages = [];
    if (messagesList.length !== 0) {
      messages = messagesList.map((value, id) => (
        <Message data={value} key={id} />
      ));
    } else {
      messages = (
        <div className={style.loading}>
          <div className={style.line1} />
          <div className={style.line2} />
          <div className={style.line3} />
        </div>
      );
    }
    return (
      <div className={style.block}>
        <div className={style.chatName}>
          {this.props.activeChat}
        </div>
        <div className={style.messagesList} onScroll={this.scrollChat}>
          {messages}
        </div>
      </div>
    );
  }

  componentDidUpdate() {
    let el = document.querySelector("." + style.messagesList);
    el.scrollTop = el.scrollHeight;
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
      sendMessage(JSON.stringify(data));
      value.target.scrollTop = 10;
    }
  };
}

export default connect(state => ({
  messagesList: state.messagesList,
  activeChat: state.activeChat
}))(ChatOutput);
