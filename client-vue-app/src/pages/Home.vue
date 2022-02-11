<template>
  <div class="carousel">
    <h2>#NEUROHACKS</h2>
    <div class="inner" ref="inner" :style="innerStyles">
      <div class="hack" v-for="hack in hacks" :key="hack.id">
        <img :src="hack.image" alt="image" />
      </div>
    </div>
    <div class="buttons">
      <button @click="right">⇷</button><button @click="left">⇸</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      hacks: [
        { image: 'https://i.imgur.com/t01bQdt.jpg' },
        { image: 'https://i.imgur.com/o03K3UB.jpg' },
        { image: 'https://i.imgur.com/V4Ryul8.jpg' },
        { image: 'https://i.imgur.com/2INuJiB.jpg' },
        { image: 'https://i.imgur.com/5gA4zSC.jpg' },
        { image: 'https://i.imgur.com/LjvZicZ.jpg' },
        { image: 'https://i.imgur.com/DtAQkfA.jpg' },
        { image: 'https://i.imgur.com/QTiVW3v.jpg' },
        { image: 'https://i.imgur.com/RGKPZP1.jpg' },
        { image: 'https://i.imgur.com/NT6w1Ih.jpg' },
        { image: 'https://i.imgur.com/3bVkk0k.jpg' }
      ],
      innerStyles: {},
      step: '',
      transitioning: false
    };
  },
  mounted() {
    this.setStep();
    this.resetTranslate();
  },
  methods: {
    setStep() {
      const innerWidth = this.$refs.inner.scrollWidth;
      const totalHacks = this.hacks.length;
      this.step = `${innerWidth / totalHacks}px`;
    },

    right() {
      if (this.transitioning) return;
      this.transitioning = true;

      this.moveRight();
      this.afterTransition(() => {
        const hack = this.hacks.shift();
        this.hacks.push(hack);
        this.resetTranslate();
        this.transitioning = false;
      });
    },
    left() {
      if (this.transitioning) return;
      this.transitioning = true;
      this.moveLeft();
      this.afterTransition(() => {
        const hack = this.hacks.pop();
        this.hacks.unshift(hack);
        this.resetTranslate();
        this.transitioning = false;
      });
    },
    afterTransition(callback) {
      const listener = () => {
        callback();
        this.$refs.inner.removeEventListener('transitioned', listener);
      };
      this.$refs.inner.addEventListener('transitionend', listener);
    },

    moveLeft() {
      this.innerStyles = {
        transform: `translateX(-${this.step})
        translateX(-${this.step})`
      };
    },
    moveRight() {
      this.innerStyles = {
        transform: `translateX(${this.step})
        translateX(-${this.step})`
      };
    },
    resetTranslate() {
      this.innerStyles = {
        transition: 'none',
        transform: `translateX(-${this.step})`
      };
    }
  }
};
</script>
<style scoped>
.carousel {
  width: 900px;
  overflow: 1;
}
h2 {
  display: flex;
  font-size: 50px;
  margin-left: 490px;
  justify-content: center;
  width: 100%;
}
.buttons {
  margin-top: 100px;
  margin-left: 900px;
  display: flex;
  justify-content: center;
}
button {
  min-width: 300px;
  min-height: 200px;
  border-radius: 20px;
  font-size: 100px;
  opacity: 80%;
  background-color: rgb(187, 76, 12);
  color: white;
  border: 5px;
  margin-right: 50px;
}
button:hover {
  font-weight: bolder;
  background-color: rgba(7, 73, 82, 0.712);
}
.inner {
  white-space: nowrap;
  transition: transform 1s;
}

.hack {
  width: 400px;
  height: 400px;
  margin-right: 190px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.hack:hover {
  transform: translateY(-10px);
}
h3 {
  color: #80cbc4;
}

img {
  max-height: 400px;
  border-radius: 15px;
}
</style>
