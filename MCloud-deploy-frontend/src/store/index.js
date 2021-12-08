import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import createPersistedState from 'vuex-persistedstate'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    // 전체 데이터
    movies: [],
    reviews: [],
    tmpUrl: '',
    // 상세 데이터
    reviewDetail: null,
    // 리뷰의 댓글들
    reviewComments: [],
    header: {},
    // 로그인 유저 이름
    loginUser: null,
    // 영화 전체 스위치 필터
    filterOptions: [],
    filterMovies: [],
    // 유저가 좋아하는 영화
    userLikeMovieList: [],
    // 유저가 작성한 리뷰
    userReviewList: [],
    // 유저가 시청한 영화
    userReviewMovieList: [],
    // 유저 좋아하는 장르
    userRecommandMoviesByLikeGenre: [],
    // 유저 영화 추천 워드 클라우드 
    userRecommandMoviesByKeyword: [],
    // 리뷰 생성 시 해당 영화 가져오기
    movieForReviewCreate: null,
    // 리뷰 업데이트 데이터
    reviewUpdateData: null,   
  },
  mutations: {
    // 영화 전체 데이터 저장
    GET_MOVIES: function (state, data) {
      state.movies = data
    },
    // 리뷰 전체 데이터 저장
    GET_REVIEWS: function (state, data) {
      state.reviews = data
    },
    // ngrok url 받아오기
    CHANGE_URL: function (state, data) {
      state.tmpUrl = data
    },
    GET_REVIEW_DETAIL: function (state, data) {
      state.reviewDetail = data
      state.reviewComments = data.comment_set
    },
    DELETE_REVIEW_DETAIL: function (state) {
      state.reviewDetail = null
    },
    SET_COMMENT: function (state, data) {
      state.reviewComments.push(data)
    },
    DELETE_COMMENT: function (state, data) {
      const idx = state.reviewComments.indexOf(data)
      state.reviewComments.splice(idx, 1)
    },
    //로그인 시 헤더값 생성
    SET_HEADER: function (state, data) {
      state.header = data
    },
    //로그아웃 시 헤더값 제거
    REMOVE_HEADER: function (state) {
      state.header = {}
    },
    SET_LOGIN_USER: function (state, data) {
      state.loginUser = data
    },
    // 영화 필터
    GET_OPTIONS: function (state, data) {
      state.filterOptions = data
    },
    // 유저가 좋아요한 영화
    USER_LIKE_MOVIE_LIST: function (state, data) {
      state.userLikeMovieList = data
    },
    // 유저에게 영화추천 (좋아요 누른 장르 기반)
    GET_RECOMMAND_MOVIES_BY_LIKE_GENRE: function (state, data) {
      state.userRecommandMoviesByLikeGenre = data
    },
    // 유저에게 영화 추천 (워드 클라우드 기반)
    GET_RECOMMAND_MOVIES_BY_KEYWORD: function (state, data) {
      state.userRecommandMoviesByKeyword = data
    },
    // 유저가 작성한 리뷰와 그 영화
    USER_REVIEW_LIST: function (state, data) {
      state.userReviewList = data
      let movies = []
      for (let movie of data) {
        movies.push(movie.movie_id)
      }
      movies = _.uniqBy(movies, "id")
      state.userReviewMovieList = movies
    },
    // 리뷰 생성 시 해당 영화 정보 가져오기
    GET_MOVIE_FOR_REVIEW_CREATE: function (state, data) {
      state.movieForReviewCreate = data
    },
    // 리뷰 생성 시 해당 영화 정보 삭제
    REMOVE_MOVIE_FOR_REVIEW_CREATE: function (state) {
      state.movieForReviewCreate = null
    },
    // 리뷰 업데이트 정보 저장
    REVIEW_UPDATE_SAVE: function (state, data) {
      state.reviewUpdateData = {
        review_pk: data.review_pk,
        title: data.title,
        content: data.content,
        rank: data.rank / 2,
        movieTitle: data.movieTitle,
        movieId: data.movieId
      }
    }
  },
  actions: {
    // movie 전체 데이터 저장
    getMovies: function ({ commit, state }) {
      axios({
        method: 'get',
        url: `${state.tmpUrl}/movies/movie`,
      })
      .then(res => {
        commit('GET_MOVIES', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    // review 전체 데이터 저장
    getReviews: function ({ commit, state }) {
      axios({
        method: 'get',
        url: `${state.tmpUrl}/community/reviews`
      })
      .then(res => {
        commit('GET_REVIEWS', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    // 영화 상세 데이터 저장
    // 리뷰 상세 데이터 저장
    // getReviewDetail: function ({ commit }, data) {
    //   commit('GET_REVIEW_DETAIL', data)
    // },
    getReviewDetail: function ({ commit, state}, review_pk) {
      axios({
        method: 'get',
        url: `${state.tmpUrl}/community/review/${review_pk}`,
        headers: state.header
      })
      .then(res => {
        commit('GET_REVIEW_DETAIL', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    // 리뷰 상세 데이터 제거
    deleteReviewDetail: function ({ commit }) {
      commit('DELETE_REVIEW_DETAIL')
    },
    // 댓글 추가
    setComment: function ({ commit }, data) {
      commit('SET_COMMENT', data)
    },
    // 댓글 삭제
    deleteComment: function ({ commit }, data) {
      commit('DELETE_COMMENT', data)
    },
    // ngrok url 바꾸기
    changeUrl: function ({ commit }, data) {
      commit('CHANGE_URL', data)
    },
    // 로그인 시 헤더값 생성
    setHeader: function ({ commit }) {
      const token = localStorage.getItem('JWT')
      const header = {
        Authorization: `Bearer ${token}`
      }
      commit('SET_HEADER', header)
    },
    //로그아웃 시 헤더값 제거
    removeHeader: function ({ commit }) {
      commit('REMOVE_HEADER')
    },
    setLoginUser: function ({ commit }, data) {
      commit('SET_LOGIN_USER', data)
    },
    // 영화 필터
    getOptions: function ({ commit }, data) {
      commit('GET_OPTIONS', data)
    },
    // 유저의 프로필페이지 요청과 응답
    getUserLikeMovieList: function ({ commit, state }, username) {
      axios({
        url: `${state.tmpUrl}/accounts/profile/${username}/profile/`,
        method: 'get',
        headers: state.header
      })
      .then(res => {
        commit('USER_LIKE_MOVIE_LIST', res.data.user_like_movies)
        commit('USER_REVIEW_LIST', res.data.user_to_review)
      })
      .catch(err => {
        console.log(err)
      })
    },
    // 유저의 좋아하는 영화 기반 추천 영화 리스트
    getRecommandMoviesByLikeGenre: function ({ commit, state }) {
      axios({
        url: `${state.tmpUrl}/movies/movie/recommand/`,
        method: 'get',
        headers: state.header
      })
      .then(res => {
        commit('GET_RECOMMAND_MOVIES_BY_LIKE_GENRE', res.data)
      })
    },
    //유저의 선택한 키워드 기반 영화 추천 리스트
    getRecommandMoviesByKeyword: function({ commit, state }) {
      axios({
        url: `${state.tmpUrl}/movies/movie/recommandBykeyword/`,
        method: 'get',
        headers: state.header
      })
      .then(res => {
        commit('GET_RECOMMAND_MOVIES_BY_KEYWORD', res.data)
      })
    },
    // 리뷰 생성 시 해당 영화 정보 가져오기 
    getMovieForReviewCreate: function ({ commit }, data) {
      commit('GET_MOVIE_FOR_REVIEW_CREATE', data)
    },
    // 리뷰 생성 시 해당 영화 정보 삭제
    removeMovieForReviewCreate: function ({ commit }) {
      commit('REMOVE_MOVIE_FOR_REVIEW_CREATE')
    },    
    // 리뷰 업데이트 정보 저장
    reviewUpdateSave: function ({commit}, data) {
      commit('REVIEW_UPDATE_SAVE', data)
    }
  },
  getters: {
    filterMovies: function (state) {
      let newMovies = state.movies
      if (state.filterOptions.length != 0) {
        for (const genre of state.filterOptions){
          newMovies = newMovies.filter(movie => {
            return (movie.genres.includes(genre))
          })
        }
      }
      return newMovies
    },
  }
})
