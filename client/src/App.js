import React, { Component } from "react";
import AuthentificationPageContainer from "./containers/AuthentificationPageContainer";
import MainPage from "./components/MainPage/MainPage";
import { connect } from "react-redux";
import LoadingPage from "./components/LoadingPage/LoadingPage";

class App extends Component {
  render() {
    const { page } = this.props;

    return (
      <div className="App">
        {page === "loading" && <LoadingPage />}
        {page === "authentification" && <AuthentificationPageContainer />}
        {page === "main" && <MainPage />}
      </div>
    );
  }
}

export default connect(state => ({ page: state.page }))(App);
