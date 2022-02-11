<template>
  <div class="carousel">
    <h2>#NEUROHACKS</h2>
    <div class="inner" ref="inner" :style="innerStyles">
      <div class="hack" v-for="hack in hacks" :key="hack.id">
        <img :src="hack.image" alt="image" />
      </div>
    </div>
    <div class="buttons">
      <div class="righty"><button @click="right">⇷</button></div>
      <div><button @click="left">⇸</button></div>
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
  overflow: 1;
  /* background-color: rgba(182, 169, 169, 0.164); */
  padding-bottom: 20px;
  /* padding-top: 20px; */
}
h2 {
  margin-top: 50px;
  padding-top: 5px;
  display: flex;
  font-size: 60px;
  justify-content: space-around;
  width: 100%;
  color: #94eee58c;
}
.buttons {
  margin-top: 80px;
  display: flex;
  justify-content: space-around;
}

button {
  min-width: 300px;
  min-height: 100px;
  border-radius: 30px;
  font-size: 100px;
  opacity: 80%;
  background-image: linear-gradient(to right, #1a4344, #3b9698, #8ecacb);
  color: white;
  border: 5px solid;
}
button:hover {
  font-weight: bolder;
  cursor: pointer;
  moz-transition: all 0.4s ease-in-out;
  -o-transition: all 0.4s ease-in-out;
  -webkit-transition: all 0.4s ease-in-out;
  transition: all 0.4s ease-in-out;
  background-image: linear-gradient(
    to right,
    rgb(238, 162, 48),
    #f0d225,
    #d68000
  );
  box-shadow: 0 4px 5px 0 rgba(16, 151, 147, 0.575);
}

.inner {
  white-space: nowrap;
  transition: transform 1s;
}

.hack {
  width: 300px;
  height: 350px;
  margin-right: 100px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.hack:hover {
  transform: translateY(-55px) translateX(-50px);
}

img {
  margin-top: 50px;
  max-height: 290px;
  border: 14px solid rgba(173, 231, 248, 0.582);
  border-radius: 30px;
}
img:hover {
  border: 14px solid rgb(173, 231, 248);
  border-radius: 30px;
  transform: scale(1.2);
  filter: brightness(110%);
}
</style>
