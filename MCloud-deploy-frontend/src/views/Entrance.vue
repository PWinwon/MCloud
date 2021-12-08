<template>
  <div>
    <entrance-login :signupClicked="signupClicked" @clickChange="clickChange" @login="login"></entrance-login>
    <entrance-signup :signupClicked="signupClicked" @clickChange="clickChange"></entrance-signup>
    <div class="a-margin">
      <a href="https://kr.lovepik.com/images/creative-22521.html">Background Png vectors by Lovepik.com</a>
    </div>
  </div>
</template>

<script>
import EntranceLogin from '@/components/entrance/EntranceLogin'
import EntranceSignup from '@/components/entrance/EntranceSignup'
export default {
  name: 'Entrance',
  components: {
    EntranceLogin,
    EntranceSignup
  },
  data: function () {
    return {
      signupClicked: false,
    }
  },
  methods: {
    clickChange: function () {
      this.signupClicked = !this.signupClicked
    },
    login: function () {
      this.$emit('login')
    }
  }
}
</script>

<style>
  .container {
  display: flex;
  justify-content: center;
  }
  .a-margin {
    margin: 20vh 0 10vh;
  }
  a:link {
    color : rgb(168, 168, 168);
  }
  a:visited {
    color : rgb(168, 168, 168);
  }
  a:hover {
    color : red;
  }
  a:active {
    color : green
  }
</style>