import React, { Component } from 'react';
import AuthentificationPage from './components/authentificationPage/authentificationPage';
import MainPage from './components/mainPage/mainPage'
import { connect } from 'react-redux';

class App extends Component {

  render() {
    let viewPage;
    switch (this.props.page){
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