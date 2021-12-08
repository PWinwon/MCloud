<template>
  <div class="parent">
    <div class="title-logo">MCloud</div>
    <div class="select-contaniner">
      <div @mouseover="movieMouseOver=true" @mouseout="movieMouseOver=false" @click="$router.push({name: 'Movie'})" class="select-btn" :class="{'is-mouse-over': movieMouseOver}">
        <p>Movie</p>
      </div>
      <div @mouseover="reviewMouseOver=true" @mouseout="reviewMouseOver=false" @click="$router.push({name: 'Review'})" class="select-btn" :class="{'is-mouse-over': reviewMouseOver}">
        <p>Review</p>
      </div>
      <div @mouseover="recommandMouseOver=true" @mouseout="recommandMouseOver=false" @click="$router.push({name: 'Recommand'})" class="select-btn" :class="{'is-mouse-over': recommandMouseOver}">
        <p>Recommand</p>
      </div>
      <div @mouseover="randomBoxMouseOver=true" @mouseout="randomBoxMouseOver=false" @click="$router.push({name: 'RandomBox'})" class="select-btn" :class="{'is-mouse-over': randomBoxMouseOver}">
        <p>RandomBox</p>
      </div>
    </div>
  </div>
</template>

<script scoped>
export default {
  name: 'Main',
  data: function () {
    return {
      movieMouseOver: false,
      reviewMouseOver: false,
      recommandMouseOver: false,
      randomBoxMouseOver: false,
    }
  }
}
</script>

<style>
  .parent {
    height: 40em;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: white;
  }
  .title-logo {
    font-size: 8em;
    -webkit-animation: tracking-in-expand 2s cubic-bezier(0.215, 0.610, 0.355, 1.000) 0.5s both;
            animation: tracking-in-expand 2s cubic-bezier(0.215, 0.610, 0.355, 1.000) 0.5s both;
    font-family: 'ghanachoco';
  }
  .select-contaniner {
    margin-top: 7em;
    display: flex;
    justify-content: center;
    -webkit-animation: text-flicker-in-glow 2s linear 1.5s both;
            animation: text-flicker-in-glow 2s linear 1.5s both;
  }
  .select-btn {
    width: 8em;
    height: 5em;
    border: 2px solid white;
    border-radius: 1.25em;
    margin: 0 2em;
    display: flex;
    flex-direction: column;
    justify-content: center;
    cursor: pointer;
    font-family: 'Vitro_core';
    /* 애니메이션 -*/
  }

  div p {
    font-weight: bold;
    font-size:1em;
    word-break:break-all;
  }
  /* jello */
  .is-mouse-over {
    -webkit-animation: jello-horizontal 0.9s both;
            animation: jello-horizontal 0.9s both;
  }
  @-webkit-keyframes jello-horizontal {
    0% {
      -webkit-transform: scale3d(1, 1, 1);
              transform: scale3d(1, 1, 1);
    }
    30% {
      -webkit-transform: scale3d(1.25, 0.75, 1);
              transform: scale3d(1.25, 0.75, 1);
    }
    40% {
      -webkit-transform: scale3d(0.75, 1.25, 1);
              transform: scale3d(0.75, 1.25, 1);
    }
    50% {
      -webkit-transform: scale3d(1.15, 0.85, 1);
              transform: scale3d(1.15, 0.85, 1);
    }
    65% {
      -webkit-transform: scale3d(0.95, 1.05, 1);
              transform: scale3d(0.95, 1.05, 1);
    }
    75% {
      -webkit-transform: scale3d(1.05, 0.95, 1);
              transform: scale3d(1.05, 0.95, 1);
    }
    100% {
      -webkit-transform: scale3d(1, 1, 1);
              transform: scale3d(1, 1, 1);
    }
  }
  @keyframes jello-horizontal {
    0% {
      -webkit-transform: scale3d(1, 1, 1);
              transform: scale3d(1, 1, 1);
    }
    30% {
      -webkit-transform: scale3d(1.25, 0.75, 1);
              transform: scale3d(1.25, 0.75, 1);
    }
    40% {
      -webkit-transform: scale3d(0.75, 1.25, 1);
              transform: scale3d(0.75, 1.25, 1);
    }
    50% {
      -webkit-transform: scale3d(1.15, 0.85, 1);
              transform: scale3d(1.15, 0.85, 1);
    }
    65% {
      -webkit-transform: scale3d(0.95, 1.05, 1);
              transform: scale3d(0.95, 1.05, 1);
    }
    75% {
      -webkit-transform: scale3d(1.05, 0.95, 1);
              transform: scale3d(1.05, 0.95, 1);
    }
    100% {
      -webkit-transform: scale3d(1, 1, 1);
              transform: scale3d(1, 1, 1);
    }
  }
  /* jello 끝 */

  /* traking */
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
  @font-face {
    font-family: 'Vitro_core';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10-21@1.0/Vitro_core.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }
  @font-face {
    font-family: 'ghanachoco';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@1.0/ghanachoco.woff') format('woff');
    font-weight: normal;
    font-style: normal;
  }
  @-webkit-keyframes text-flicker-in-glow {
    0% {
      opacity: 0;
    }
    10% {
      opacity: 0;
      text-shadow: none;
    }
    10.1% {
      opacity: 1;
      text-shadow: none;
    }
    10.2% {
      opacity: 0;
      text-shadow: none;
    }
    20% {
      opacity: 0;
      text-shadow: none;
    }
    20.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.25);
    }
    20.6% {
      opacity: 0;
      text-shadow: none;
    }
    30% {
      opacity: 0;
      text-shadow: none;
    }
    30.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.45), 0 0 60px rgba(255, 255, 255, 0.25);
    }
    30.5% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.45), 0 0 60px rgba(255, 255, 255, 0.25);
    }
    30.6% {
      opacity: 0;
      text-shadow: none;
    }
    45% {
      opacity: 0;
      text-shadow: none;
    }
    45.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.45), 0 0 60px rgba(255, 255, 255, 0.25);
    }
    50% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.45), 0 0 60px rgba(255, 255, 255, 0.25);
    }
    55% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.45), 0 0 60px rgba(255, 255, 255, 0.25);
    }
    55.1% {
      opacity: 0;
      text-shadow: none;
    }
    57% {
      opacity: 0;
      text-shadow: none;
    }
    57.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.35);
    }
    60% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.35);
    }
    60.1% {
      opacity: 0;
      text-shadow: none;
    }
    65% {
      opacity: 0;
      text-shadow: none;
    }
    65.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.35), 0 0 100px rgba(255, 255, 255, 0.1);
    }
    75% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.35), 0 0 100px rgba(255, 255, 255, 0.1);
    }
    75.1% {
      opacity: 0;
      text-shadow: none;
    }
    77% {
      opacity: 0;
      text-shadow: none;
    }
    77.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.4), 0 0 110px rgba(255, 255, 255, 0.2), 0 0 100px rgba(255, 255, 255, 0.1);
    }
    85% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.4), 0 0 110px rgba(255, 255, 255, 0.2), 0 0 100px rgba(255, 255, 255, 0.1);
    }
    85.1% {
      opacity: 0;
      text-shadow: none;
    }
    86% {
      opacity: 0;
      text-shadow: none;
    }
    86.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.6), 0 0 60px rgba(255, 255, 255, 0.45), 0 0 110px rgba(255, 255, 255, 0.25), 0 0 100px rgba(255, 255, 255, 0.1);
    }
    100% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.6), 0 0 60px rgba(255, 255, 255, 0.45), 0 0 110px rgba(255, 255, 255, 0.25), 0 0 100px rgba(255, 255, 255, 0.1);
    }
  }
  @keyframes text-flicker-in-glow {
    0% {
      opacity: 0;
    }
    10% {
      opacity: 0;
      text-shadow: none;
    }
    10.1% {
      opacity: 1;
      text-shadow: none;
    }
    10.2% {
      opacity: 0;
      text-shadow: none;
    }
    20% {
      opacity: 0;
      text-shadow: none;
    }
    20.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.25);
    }
    20.6% {
      opacity: 0;
      text-shadow: none;
    }
    30% {
      opacity: 0;
      text-shadow: none;
    }
    30.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.45), 0 0 60px rgba(255, 255, 255, 0.25);
    }
    30.5% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.45), 0 0 60px rgba(255, 255, 255, 0.25);
    }
    30.6% {
      opacity: 0;
      text-shadow: none;
    }
    45% {
      opacity: 0;
      text-shadow: none;
    }
    45.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.45), 0 0 60px rgba(255, 255, 255, 0.25);
    }
    50% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.45), 0 0 60px rgba(255, 255, 255, 0.25);
    }
    55% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.45), 0 0 60px rgba(255, 255, 255, 0.25);
    }
    55.1% {
      opacity: 0;
      text-shadow: none;
    }
    57% {
      opacity: 0;
      text-shadow: none;
    }
    57.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.35);
    }
    60% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.35);
    }
    60.1% {
      opacity: 0;
      text-shadow: none;
    }
    65% {
      opacity: 0;
      text-shadow: none;
    }
    65.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.35), 0 0 100px rgba(255, 255, 255, 0.1);
    }
    75% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.35), 0 0 100px rgba(255, 255, 255, 0.1);
    }
    75.1% {
      opacity: 0;
      text-shadow: none;
    }
    77% {
      opacity: 0;
      text-shadow: none;
    }
    77.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.4), 0 0 110px rgba(255, 255, 255, 0.2), 0 0 100px rgba(255, 255, 255, 0.1);
    }
    85% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.55), 0 0 60px rgba(255, 255, 255, 0.4), 0 0 110px rgba(255, 255, 255, 0.2), 0 0 100px rgba(255, 255, 255, 0.1);
    }
    85.1% {
      opacity: 0;
      text-shadow: none;
    }
    86% {
      opacity: 0;
      text-shadow: none;
    }
    86.1% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.6), 0 0 60px rgba(255, 255, 255, 0.45), 0 0 110px rgba(255, 255, 255, 0.25), 0 0 100px rgba(255, 255, 255, 0.1);
    }
    100% {
      opacity: 1;
      text-shadow: 0 0 30px rgba(255, 255, 255, 0.6), 0 0 60px rgba(255, 255, 255, 0.45), 0 0 110px rgba(255, 255, 255, 0.25), 0 0 100px rgba(255, 255, 255, 0.1);
    }
  }

</style>