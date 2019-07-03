import React from "react";
import { connect } from "react-redux";
import style from "./chatOutput.module.css";
import { socket } from "../../websockets/websocket";
import Message from "../message/message";

class ChatOutput extends React.Component {

  render() {
    const { messagesList } = this.props;
    let messages = [];
    if (messagesList.length !== 0) {
      messages = messagesList.map((value, id) => (
        <Message data={value} key={id} />
      ));
    }
    return (
      <div className={style.output}>
        <div className={style.nameChat}>
          {this.props.activeChat}
          <div className={style.deleteButton} onClick={this.deleteChat}>Очистить чат</div>
        </div>
        <div className={style.messagesList} onScroll={e => this.scrollChat(e)}>
          {messages}
        </div>
      </div>
    );
  }

  componentDidMount() {
    let el = document.querySelector("." + style.messagesList);
    el.scrollTop = el.scrollHeight;
    this.setState({
      muteSound: false
    })
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

  deleteChat = () =>{
    const data ={
      Type: 'chat',
      Command: 'purge'
    }
    socket.send(JSON.stringify(data));
  }
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
