<template>
  <div>
    <div v-if="signupClicked===true" class="log-box-container"> 
      <h2 style="color: white;">Signup</h2>
      <div class="log-form-box">
        <div>
          <p class="info-p">Username</p>
          <input class="type-style" type="text" placeholder="Username" v-model="credentials.username">
        </div>
        <div class="make-position">
          <p class="info-p">Password</p>
          <input class="type-style" type="password" placeholder="Password" v-model="credentials.password">
          <div v-if="passwordLengthCheck === false" class="error-message">
            비밀번호를 8자리 이상 입력해주세요.
          </div>
        </div>
        <div class="make-position">
          <p class="info-p">Password confirm</p>
          <input class="type-style" type="password" placeholder="Password" @keyup.enter="signup" v-model="credentials.password2">
          <div v-if="passwordEqualCheck === false" class="error-message">
            비밀번호가 맞지 않습니다.
          </div>
        </div>
        <div class="make-position">
          <vs-button v-if="passwordLengthCheck && passwordEqualCheck" class="signup-btn" color="rgb(59,222,200)" gradient @click="signup">
            회원가입
          </vs-button>
          <vs-button v-else class="signup-btn" color="rgb(59,222,200)" disabled gradient @click="signup">
            회원가입
          </vs-button>
          <div v-if="isValid === false" class="error-message" style="top: 2.3em;">
            이미 사용 중인 아이디입니다.
          </div>
        </div>
        <span class="switch-log" @click="goLogin">계정이 있으신가요?</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'EntranceSignup',
  props: {
    signupClicked: Boolean
  },
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        password2: ''
      },
      isValid: true,
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: `${this.tmpUrl}/accounts/signup/`,
        data: this.credentials
      })
      .then(() => {
        this.goLogin()
      })
      .catch(err => {
        console.log(err)
        if (err.response.status === 400) {
          this.isValid = false
        }
      })
    },
    goLogin: function () {
      this.credentials.username = ''
      this.credentials.password = ''
      this.credentials.password2 = ''
      this.$emit('clickChange')
    }
  },
  computed: {
    ...mapState([
      'tmpUrl'
    ]),
    passwordEqualCheck: function () {
      if (this.credentials.password === this.credentials.password2 || this.credentials.password2.length < 8) {
        return true
      }
      else {
        return false
      }
    },
    passwordLengthCheck: function () {
      if (this.credentials.password.length > 7 || this.credentials.password.length === 0) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style>
  div div {
    font-family: 'Pretendard-Regular';
  }
  .signup-form-box {
    display: flex;
    flex-direction: column;
    width: 40rem;
    justify-content: flex-end;
    align-items: center;
    margin: 2em auto 0;
  }
  .info-p {
    margin: 0;
    text-align: left;
  }
  .type-style {
    border: 1px solid lightgray;
    border-radius: 0.5em;
    height: 2.5em;
    width: 16em;
    margin: 0 0 1.5em;
    font-family: 'Pretendard-Regular';
  }
  .error-message {
    font-size: 14px;
    color: rgb(255, 75, 75);
    position: absolute;
    top: 4em;
  }
  .signup-btn {
    width: 13em;
    margin: 0 0 1.5em;
    position: relative;
  }
  .switch-log {
    margin-top: 0.25em;
    font-size: 14px;
    text-decoration: underline;
    color: rgb(0, 238, 255);
    cursor: pointer;
  }
  .make-position {
    position: relative;
  }
</style>