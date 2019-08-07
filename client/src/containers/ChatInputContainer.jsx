import React, { Component } from "react";
import { connect } from "react-redux";
import ChatInput from "../components/MainPage/ChatContainer/ChatInput/ChatInput";
import { setImageAction, replyAction } from "../actions/";

class ChatInputContainer extends Component {
  render() {
    const { setImage, image, replyMessage, reply } = this.props;
    return <ChatInput setImage={setImage} image={image} replyMessage={replyMessage} reply={reply} />;
  }
}

export default connect(
  state => ({
    image: state.image,
    replyMessage: state.replyMessage
  }),
  {
    reply: replyAction,
    setImage: setImageAction
  }
)(ChatInputContainer);
