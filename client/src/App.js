import React, { Component } from 'react';
import AuthentificationPage from './components/AuthentificationPage/AuthentificationPage.jsx';
import MainPage from './components/MainPage/MainPage'
import { connect } from 'react-redux';
import LoadingPage from './components/LoadingPage/LoadingPage';

class App extends Component {

  render() {
    let viewPage;
    switch (this.props.page){
      case 'loading': {
        viewPage = <LoadingPage />;
        break;
      }
      case 'authentification': {
        viewPage = <AuthentificationPage />;
        break;
      }
      case 'main':{
        viewPage = <MainPage />;
        break;
      }
      default: break;
    }

    return (
      <div className="App">
        {viewPage}
      </div>
    );
  }
}

const mapStateToProps = store => {
  return {
    page: store.page
  }
}

export default connect(mapStateToProps)(App)