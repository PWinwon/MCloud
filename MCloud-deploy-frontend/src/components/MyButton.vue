<template>
  <div class="balloon">
    <p @click="goMyProfile">Mypage</p>
    <hr style="width: 100%; margin: 0;">
    <p @click="logout">Logout</p>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'MyButton',
  methods: {
    logout: function () {
      this.$emit('logout')
    },
    goMyProfile: function () {
      this.$router.push({ name: 'Profile', params: {username: this.loginUser}}).catch(() => {})
    }
  },
  computed: {
    ...mapState([
      'loginUser'
    ])
  }
}
</script>

<style scoped>
  .balloon {  
    width:150px; 
    height:100px;
    background: white; 
    border: 1px solid lightgray;
    border-radius: 10px;
    position: absolute;
    display: flex;
    right: -3.5em;
    top: 3.2em;
    flex-direction: column;
    font-size: 1rem;
  }
  .balloon:after { 
    border-top:0px solid transparent; 
    border-left: 10px solid transparent; 
    border-right: 10px solid transparent; 
    border-bottom: 10px solid white; 
    content:""; 
    position:absolute;
    top:-0.5rem;
    left:65px;  
  }
  div p {
    height: 30px;
    color: rgb(153, 153, 153);
    cursor: pointer;
  }
</style>