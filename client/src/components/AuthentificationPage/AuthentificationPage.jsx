import React from "react";
import style from "./AuthentificationPage.module.css";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import {
  setPage,
  setLogin,
  setPassword,
  removeLogin,
  removePassword
} from "../../actions/actions.js";
import sendMessage from "../../websockets/websocket";

class AuthentificationPage extends React.Component {
  render() {
    return (
        <div className={style.page}>
          <div className={style.layout}>
            <p className={style.title}>Добро пожаловать</p>
            <p>Логин</p>
            <input
              type="text"
              className={style.input}
              onChange={event => this.props.setLogin(event.target.value)}
              onClick={removeLogin}
              value={this.props.login}
              maxLength={20}
              placeholder="Введите логин"
            />
            <p>Пароль</p>
            <input
              placeholder="Введите пароль"
              type="password"
              className={style.input}
              onChange={event => this.props.setPassword(event.target.value)}
              value={this.props.password}
              onClick={() => this.props.removePassword()}
              maxLength={30}
            />
            <div className={style.button} onClick={() => this.goToPage()}>
              Войти
            </div>
            <div className={style.button} onClick={() => this.registration()}>
              Регистрация
            </div>
          </div>
        </div>
    );
  }

  goToPage = () => {
    if (this.props.login !== "" && this.props.password !== "") {
      let data = {
        Type: "account",
        Command: 'login',
        Login: this.props.login,
        Password: this.props.password
      };
      data = JSON.stringify(data);
      sendMessage(data);
    }
  };

  registration = () => {
    if (this.props.login !== "" && this.props.password !== "") {
      let data = {
        Type: "account",
        Command: 'registration',
        Login: this.props.login,
        Password: this.props.password
      };
      data = JSON.stringify(data);
      sendMessage(data);
    }
  };
}

const mapStateToProps = store => {
  return {
    login: store.login,
    password: store.password
  };
};

const mapDispatchToProps = dispatch => {
  return bindActionCreators(
    {
      setPage: setPage,
      setLogin: setLogin,
      setPassword: setPassword,
      removeLogin: removeLogin,
      removePassword: removePassword
    },
    dispatch
  );
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(AuthentificationPage);
