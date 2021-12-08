<template>
  <div>
    <div class="example-3d">
      <swiper class="swiper" :options="swiperOption">
        <swiper-slide 
          v-for="movie in userRecommandMoviesByLikeGenre"
          :key=movie.id
        >
          <recommand-movie-list-first-item
            :movie="movie"
          ></recommand-movie-list-first-item>
        </swiper-slide>
        <div class="swiper-pagination" slot="pagination"></div>
      </swiper>
    </div>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'
import { mapState } from 'vuex'


import RecommandMovieListFirstItem from '@/components/recommand/RecommandMovieListFirstItem'

export default {
  name: 'RecommandMovieListFirst',
  components: {
    RecommandMovieListFirstItem,
    Swiper,
    SwiperSlide
  },
  computed: {
    ...mapState([
      'userRecommandMoviesByLikeGenre',
    ])
  },
  data() {
    return {
      swiperOption: {
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        coverflowEffect: {
          rotate: 50,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows : true
        },
        pagination: {
          el: '.swiper-pagination'
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
  .example-3d {
    width: 100vw;
    height: 400px;
    padding-top: 50px;
    padding-bottom: 50px;
  }

  .swiper {
    height: 100%;
    width: 100%;

    .swiper-slide {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 300px;
      height: 300px;
      text-align: center;
      font-weight: bold;
      // font-size: $font-size-huge * 2;
      // background-color: #2C8DFB;
      // background-position: center;
      // background-size: cover;
      // overflow: hidden;
      // color: $white;
    }
  }
</style>