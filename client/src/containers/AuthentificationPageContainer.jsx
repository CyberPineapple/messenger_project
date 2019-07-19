import React, { Component } from 'react'
import { connect } from 'react-redux'
import AuthentificationPage from '../components/AuthentificationPage/AuthentificationPage';
import { setPasswordAction, setLoginAction } from '../actions/'

export class AuthentificationPageContainer extends Component {

  render() {
    const { login, password, setLogin, setPassword } = this.props;
    return (
      <AuthentificationPage login={login} password={password} setLogin={setLogin} setPassword={setPassword} />
    )
  }
}

const mapStateToProps = (state) => ({
  login: state.user.login,
  password: state.user.password
})

const mapDispatchToProps = {
  setLogin: setLoginAction, setPassword: setPasswordAction
}

export default connect(mapStateToProps, mapDispatchToProps)(AuthentificationPageContainer);