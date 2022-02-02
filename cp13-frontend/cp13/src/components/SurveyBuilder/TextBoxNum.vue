<template>
  <div class="button-row">
    <input
      type="number"
      v-model="compQuery"
      :placeholder="placeholder"
      @blur="update"
    />
    <button-base class="primary square" :icon="'fas fa-minus fa-me'" @buttonPress="decrement"/>
    <button-base class="primary square" :icon="'fas fa-plus fa-me'" @buttonPress="increment" style="margin-left: 0px;" />
  </div>
</template>

<script>
import ButtonBase from '../../components/ButtonBase.vue';
export default {
  components: { ButtonBase },
  name: "TextBoxNum",
  data() {
    
    return {
      query: this.value,
    };
  },
  props: {
    placeholder: String,
    initialValue: String,
    value: String,
  },
  methods: {
      /**
       * Update the text box number
       */
      update: async function () {
          await this.$emit('update', parseInt(this.query));
          this.query = this.value;
      },
      /**
       * Increment the text box number
       */
      increment: async function () {
          await this.$emit('increment');
          this.query = this.value;
      },
      /**
       * Decrement the text box number
       */
      decrement: async function () {
          await this.$emit('decrement');
          this.query = this.value;
      }
  },
  computed: {
    compQuery: {
      get() {
        return this.query;
      },
      set(newValue) {
        this.query = newValue;
      }
    }
  }
};
</script>

<style scoped>
html:lang(ur) * {
  text-align: right;
}

input[type="number"] {
  /* padding: 0; */
  height: 48px;
  /* width: calc(100% - 32px); */
  /* width: 100%; */
  box-sizing: border-box;
  position: relative;
  left: 0;
  outline: none;
  background-color: white;
  font-size: 16px;

  padding: 8px;
  border: 2px solid #eff2f5;
  border-radius: 4px;
}

input[type="number"]:focus {
  border: 2px solid #566370;
}

.button-row {
  padding: 8px 16px;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: center;

}

</style>
