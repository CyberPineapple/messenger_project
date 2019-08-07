import React, { Component } from "react";
import { connect } from "react-redux";
import ChatMenu from "../components/MainPage/ChatMenu/ChatMenu";

class ChatMenuContainer extends Component {
  render() {
    const { usersOnline } = this.props;
    return <ChatMenu usersOnline={usersOnline} />;
  }
}

const mapStateToProps = state => ({
  usersOnline: state.usersOnline
});

const mapDispatchToProps = {};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ChatMenuContainer);
