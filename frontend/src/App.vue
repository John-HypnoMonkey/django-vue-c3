<template>
  <div>
    <vue-c3 :handler="handler"></vue-c3>
  </div>
</template>

<script>
import Vue from 'vue'
import VueC3 from 'vue-c3'
import axios from 'axios'
import VueTimers from 'vue-timers'

Vue.use(VueTimers)
let postid = '0'
export default {
  name: 'App',
  methods: {
    getAPI () {
      axios.get(`http://127.0.0.1:8000/api/chart/${postid}`)
        .then(response => {
          this.handler.$emit('dispatch',
            (chart) => chart.flow({
              columns: [
                ['likes', response.data['likes']],
                ['reposts', response.data['reposts']],
                ['comments', response.data['comments']]
              ]
            }))
          postid = response.data['post_id']
        })
    }
  },
  components: {
    VueC3
  },
  created () {
    this.$options.interval = setInterval(this.getAPI, 3000)
  },
  mounted () {
    const options = {
      data: {
        columns: [
          ['likes', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          ['reposts', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          ['comments', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
      }
    }
    this.handler.$emit('init', options)
  },
  beforeDestroy () {
    clearInterval(this.$options.interval)
  },
  data () {
    return {
      handler: new Vue()
    }
  }
}
</script>
