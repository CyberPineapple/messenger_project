import React, { PureComponent } from "react";
import style from "./AuthentificationPage.module.css";
import sendMessage from "../../websockets/websocket";

export default class AuthentificationPage extends PureComponent {
  handleChangeLoginField = e => {
    this.props.setLogin(e.target.value);
  };

  handleClickLoginField = () => {
    this.props.setLogin("");
  };

  handleCLickPasswordField = () => {
    this.props.setPassword("");
  };

  handleChangePasswordField = e => {
    this.props.setPassword(e.target.value);
  };

  authorization = () => {
    const { login, password } = this.props;
    if (login !== "" && password !== "") {
      let data = {
        Type: "account",
        Command: "login",
        Login: login,
        Password: password
      };
      data = JSON.stringify(data);
      sendMessage(data);
    }
  };

  registration = () => {
    const { login, password } = this.props;
    if (login !== "" && password !== "") {
      let data = {
        Type: "account",
        Command: "registration",
        Login: login,
        Password: password
      };
      data = JSON.stringify(data);
      sendMessage(data);
    }
  };

  render() {
    const { login, password } = this.props;

    return (
      <div className={style.page}>
        <div className={style.layout}>
          <p className={style.title}>Добро пожаловать</p>
          <p>Логин</p>
          <input
            type="text"
            name="login"
            autoComplete="on"
            className={style.input}
            onChange={this.handleChangeLoginField}
            onClick={this.handleClickLoginField}
            value={login}
            maxLength={20}
            placeholder="Введите логин"
          />
          <p>Пароль</p>
          <input
            placeholder="Введите пароль"
            type="password"
            name="password"
            autoComplete="on"
            className={style.input}
            onChange={this.handleChangePasswordField}
            value={password}
            onClick={this.handleCLickPasswordField}
            maxLength={30}
          />
          <button className={style.button} onClick={this.authorization}>
            Войти
          </button>
          <button className={style.button} onClick={this.registration}>
            Регистрация
          </button>
        </div>
      </div>
    );
  }
}
