<template>
  <div class="carousel">
    <div class="inner">
      <div class="hack" v-for="hack in hacks" :key="hack">
        {{ hack }}
      </div>
    </div>


  <button @click="right">right</button>
  <button>left</button>

</template>

<script>
export default {
  name: 'Home',
data () {
    return {
      hacks: [1, 2, 3, 4, 5, 6, 7, 8],
      innerStyles: {},
      step: ''
    }
  },
  mounted () {
    this.setStep()
  },
  methods: {
    setStep () {
      const innerWidth = this.$refs.inner.scrollWidth 
      const totalHacks = this.hacks.length
      this.step = `${innerWidth / totalHacks}px` 
    },

    right () {
      this.moveRight() 
      this.afterTransition(() => {
        const hack = this.hacks.shift()
        this.hacks.push(hack)
      })
    },

    afterTransition(callback) {
      const listener = () => {
        callback()
        this.$refs.inner.removeEventListener('transitioned', listener)
      }
    this.$refs.inner.addEventListener('transitionend', listener)
    },

    moveLeft () {
      this.innerStyles = {
        transform: `translateX(-${this.step})`
    }
  }
  }
}
</script>
<style scoped>
.carousel {
  width: 300px;
  overflow: hidden;
}

.inner {
  white-space: nowrap;
  transition: transform 0.2s;
}

.hack {
  width: 100px;
  height: 100px;
  margin-right: 20px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
h3 {
  color: #80cbc4;
}

.image-container-grid {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: space-around;
}

img {
  max-height: 200px;
  border-radius: 7px;
}
</style>
