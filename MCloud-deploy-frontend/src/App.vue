<template>
  <div id="app" :style="{'background-image':'url(' + require('@/assets/spotlight.jpg') + ')'}" class="base-style" :class="{'fade-in':isMain}">
    <div id="nav">
      <div v-if="isLogin" class="nav-son" >
        <div class="nav-son-first">
          <router-link :to="{ name: 'Main' }" @click="goMain">
            <img src="@/assets/mcloudlogo.png" alt="" style="width: 100%; height: auto;">
          </router-link> 
        </div>
        <div class="nav-son-center">
          <router-link :to="{ name: 'Movie' }">Movie</router-link>
          <router-link :to="{ name: 'Review' }">Review</router-link>
          <router-link :to="{ name: 'Recommand' }">Recommand</router-link>
          <router-link :to="{ name: 'RandomBox' }">RandomBox</router-link>
        </div>
        <div class="nav-son-last">
          <i class="fas fa-user-circle fa-2x" style="color: white; cursor: pointer; position: relative;" @click="openButton" v-click-outside="closeButton">
            <my-button v-if="isButtonOn" @logout="logout"></my-button>
          </i>
        </div>
      </div>
    </div>

    <div class="content-style">

      <router-view @login="setLogin" @goMain="notMain"/>
    </div>
  </div>
</template>
<script>
import vClickOutside from 'v-click-outside'

import { mapState } from 'vuex'

import MyButton from '@/components/MyButton'

export default {
  directives: {
    clickOutside: vClickOutside.directive
  },
  components: {
    MyButton
  },
  data: function () {
    return {
      movies: [],
      isLogin: false,
      isButtonOn: false,
      isMain: false,
    }
  },
  methods: {
    setLogin: function () {
      this.isLogin = true
      this.isMain = true
    },
    logout: function () {
      localStorage.removeItem('JWT')
      this.isLogin = false
      this.isMain = false
      this.$store.dispatch('removeHeader')
      this.$router.push({ name: 'Entrance' })
    },
    openButton: function () {
      this.isButtonOn = !this.isButtonOn
    },
    closeButton : function () {
      this.isButtonOn = false
    },
    goMain: function () {
      this.isMain = true
    },
    notMain: function () {
      this.isMain = false
    }
  },
  created: function () {
    // serializer 데이터 받아오기
    // if (this.movies.length === 0) {
    //   this.$store.dispatch('getMovies')
    // }
    // this.$store.dispatch('getReviews')
    // 로그인 체크
    if (localStorage.getItem('JWT')) {
      this.isLogin = true
    } else {
      localStorage.removeItem('JWT')
      this.$router.push({ name: 'Entrance'}).catch(() => {})
    }
    this.$store.dispatch('changeUrl', 'https://readyofcourse.herokuapp.com')
    this.$store.dispatch('getRecommandMoviesByKeyword')
  },
  computed: {
    ...mapState([
      'loginUser',
    ])
  }
}
</script>

<style>
  html {
      width: 100%;
      height: 100%;
      display: table;
  }

  body {
      width: 100%;
      display: table-cell;
  }
  
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #193149;
    height: 100%;
    border-radius: 20px;
  }

  #nav {
    font-size: 1.3em;
    padding: 30px;
    background-color: rgba(255, 255, 255, 0);
    border-radius: 20px;
    margin-bottom: 10px;
  }
  .nav-son {
    display: flex;
    align-items: center;
  }
  .nav-son-first {
    flex: 1;
  }
  .nav-son-center {
    flex: 6;
    display: flex;
    justify-content: center;
  }
  .nav-son-last {
    flex: 1;
  }
  #nav a {
    font-weight: bold;
    color: white;
    padding: 0 4rem;
    text-decoration: none;
    margin: auto 0;
  }

  #nav a.router-link-exact-active {
    color: #55D5FF;
  }
  .left {
    text-align: left;
  }
  .container {
    display: flex;
    justify-content: center;
  }
  @font-face {
    font-family: 'GowunBatang-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2108@1.1/GowunBatang-Regular.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }

  .content-style {
    border-radius: 30px;
  }
  
  .rd-button {
    border: none;
    border-radius: 1rem;
    font-family: 'Pretendard-Regular';
    width: 3rem;
    height: 2rem;
    margin: 0.2rem;
  }
  div div {
    font-family: 'Pretendard-Regular';
  }
  @font-face {
    font-family: 'Pretendard-Regular';
    src: url('https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
    font-weight: 400;
    font-style: normal;
  }
  .base-style {
    height: 100vh;
    background-repeat : no-repeat;
    background-position: center top;
    background-size : contain;
  }
  /* 로그인 배경화면 */
  .tracking-in-expand {
    -webkit-animation: tracking-in-expand 2s linear 0.3s both;
            animation: tracking-in-expand 2s linear 0.3s both;
  }
  @-webkit-keyframes tracking-in-expand {
    0% {
      letter-spacing: -0.5em;
      opacity: 0;
    }
    40% {
      opacity: 0.6;
    }
    100% {
      opacity: 1;
    }
  }
  @keyframes tracking-in-expand {
    0% {
      letter-spacing: -0.5em;
      opacity: 0;
    }
    40% {
      opacity: 0.6;
    }
    100% {
      opacity: 1;
    }
  }
  .fade-in {
    -webkit-animation: fade-in 3s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
            animation: fade-in 3s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
  }
  @-webkit-keyframes fade-in {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }
  @keyframes fade-in {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }


</style>