<template>
  <div>
    <div v-if="signupClicked===false" class="log-box-container"> 
      <h2 style="color: white;">Login</h2>
      <div class="log-form-box">
        <div>
          <p class="info-p">Username</p>
          <input class="type-style" type="text" placeholder="Username" v-model="credentials.username">
        </div>
        <div>
          <p class="info-p">Password</p>
          <input class="type-style" type="password" placeholder="Password" @keyup.enter="login" v-model="credentials.password">
        </div>
        <div v-if="isValid === false" class="login-failed">
          아이디와 비밀번호를 확인해주세요.
        </div>
        <vs-button class="login-btn" color="rgb(59,222,200)" gradient @click="login">로그인</vs-button>
        <span class="switch-log" @click="goSignup">계정이 없으신가요?</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'EntranceLogin',
  props: {
    signupClicked: Boolean
  },
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      },
      isValid: true,
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: `${this.tmpUrl}/accounts/api/token/`,
        data: this.credentials
      })
      .then(res => {
        localStorage.setItem('JWT', res.data.access)
        this.$emit('login')
        this.$store.dispatch('setHeader')
        this.$store.dispatch('setLoginUser',this.credentials.username)
        this.$router.push({ name: 'Main' })
      })
      .catch(err => {
        this.isValid = false
        console.log(err)
      })
    },
    goSignup: function () {
      this.credentials.username = ''
      this.credentials.password = ''
      this.isValid = true
      this.$emit('clickChange')
    }
  },
  created: function () {
     this.isValid = true
  },
  computed: {
    ...mapState([
      'tmpUrl'
    ])
  }
}
</script>

<style>
  div div {
    font-family: 'Pretendard-Regular';
  }
  .log-box-container {
    width: 20em;
    height: 23em;
    text-align: center;
    background-color: #bed8f548;;
    padding: 2em 0;
    margin: 5em auto 0;
    border-radius: 1em;
  }
  .log-form-box {
    display: flex;
    flex-direction: column;
    justify-content: en;
    align-items: center;
    margin: 0 auto;
  }
  .info-p {
    color: rgb(255, 255, 255);
    margin: 0;
    text-align: left;
  }
  .type-style {
    border: 1px solid lightgray;
    border-radius: 0.5em;
    height: 2.5em;
    width: 16em;

    font-family: 'Pretendard-Regular';
  }
  .login-failed {
    font-size: 14px;
    color: rgb(255, 75, 75);
  }
  .login-btn {
    width: 13em;
  }
  .go-signup {
    font-size: 12px;
    text-decoration: underline;
    color: rgb(79, 115, 212);
    cursor: pointer;
  }
</style>