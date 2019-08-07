import React, { Component } from "react";
import { connect } from "react-redux";
import ChatOutput from "../components/MainPage/ChatContainer/ChatOutput/ChatOutput";
import { replyAction } from "../actions/actions";

export class ChatOutputContainer extends Component {
  render() {
    const { messagesList, activeChat, reply, replyMessage } = this.props
    return <ChatOutput messagesList={messagesList} activeChat={activeChat} reply={reply} replyMessage={replyMessage} />;
  }
}

const mapStateToProps = state => ({
  messagesList: state.messagesList,
  activeChat: state.activeChat,
  replyMessage: state.replyMessage
});

const mapDispatchToProps = {
  reply: replyAction
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ChatOutputContainer);
