import React, { Component } from "react";
import AuthentificationPage from "./components/AuthentificationPage/AuthentificationPage.jsx";
import MainPage from "./components/MainPage/MainPage";
import { connect } from "react-redux";
import LoadingPage from "./components/LoadingPage/LoadingPage";

class App extends Component {
  render() {
    const { page } = this.props;

    return (
      <div className="App">
        {page === "loading" && <LoadingPage />}
        {page === "authentification" && <AuthentificationPage />}
        {page === "main" && <MainPage />}
      </div>
    );
  }
}

export default connect(state => ({ page: state.page }))(App);
