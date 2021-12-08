<template>
  <div>
    <div :id="'word-cloud-'+movie.id" @click="goMovieDetail">
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'RandomBoxCubeItem',
  props: {
    movie: Object,
  },
  data() {
    return {
      words: [],
    };
  },
  created: function () {
    const wordList = []
    for (let keyword of this.movie.movie_keywords) {
      const mydata = {
        text: keyword.word,
        size: keyword.count
      }
      wordList.push(mydata)
    }
    this.words = wordList
  },
  mounted() {
    if (this.movie.movie_keywords.length != 0) {
      this.genLayout();
    }
  },
  methods: {
    genLayout() {
      const cloud = require('d3-cloud');
      cloud()
        .words(this.words)
        .padding(1)
        .font('Impact')
        .fontSize(function (d) {
          return d.size * 2;
        })
        .on('end', this.end)
        .spiral('archimedean')
        .start()
        .stop();
    },
    end(words) {
      const d3 = require('d3');
      const width = 600;
      const height = 600;
      d3.select(`#word-cloud-${this.movie.id}`)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .style('background', 'rgba(255, 255, 255, 0)')
        .append('g')
        .attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')') // g를 중심에서 단어들을 그리기 때문에 g를 svg 중심으로 이동
        .selectAll('text')
        .data(words)
        .enter()
        .append('text')
        .style('font-size', (d) => {
          return d.size + 'px';
        })
        .style('font-family', 'Impact')
        .style('fill', () => {
          const r = parseInt(Math.random() * 255);
          const g = parseInt(Math.random() * 255);
          const b = parseInt(Math.random() * 255);
          return `rgb(${r}, ${g}, ${b})`;
        })
        .attr('text-anchor', 'middle')
        .attr('transform', (d) => {
          return 'translate(' + [d.x, d.y] + ')rotate(' + d.rotate + ')';
        })
        .text((d) => d.text);
    },
    goMovieDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: {movie_pk: this.movie.id}})
    },
  },
}
</script>

<style>

</style>