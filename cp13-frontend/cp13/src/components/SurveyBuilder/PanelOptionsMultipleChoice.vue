<template>
  <div class="options">
    <h1 class="close-header">{{ $t('pOptionsMC.numOptions') }}</h1>
    <!-- This is the actual number field -->
    <text-box-num
      :value="question.choices.length.toString()"
      :key="question.choices.length"
      @update="
        (value) =>
          $store.commit('updateMultiList', { question: question, value: value })
      "
      @increment="insertNewElement($store)"
      @decrement="removeLastElement($store)"
    />
    <line-base class="dark" />
    <div class="text-with-button">
      <!-- The answer required toggle -->
      <h2>{{ $t('pOptionsMC.allowMultiple') }}</h2>
      <toggle-base
        :toggled="question.multipleAnswers"
        @handleToggle="
          $store.commit('toggle', { parent: question, key: 'multipleAnswers' })
        "
      ></toggle-base>
    </div>
    <div v-if="question.multipleAnswers">
      <!-- This is for multiple answers -->
      <line-base class="light" />
      <h1 class="close-header">{{ $t('pOptionsMC.setMinimum') }}</h1>
      <text-box-num
        :value="question.minChoices != null ? question.minChoices.toString() : ''"
        :key="question.minChoices"
        @update="
          (value) =>
            $store.commit('updateValue', {
              parent: question,
              key: 'minChoices',
              value: value,
            })
        "
        @increment="
          $store.commit('updateValue', {
            parent: question,
            key: 'minChoices',
            value: parseInt(question.minChoices) + 1,
          })
        "
        @decrement="
          $store.commit('updateValue', {
            parent: question,
            key: 'minChoices',
            value: parseInt(question.minChoices) - 1,
          })
        "
      />
      <line-base class="light" />
      <h1 class="close-header">{{ $t('pOptionsMC.setMaximum') }}</h1>
      <text-box-num
        :value="question.maxChoices != null ? question.maxChoices.toString() : ''"
        :key="question.maxChoices"
        @update="
          (value) =>
            $store.commit('updateValue', {
              parent: question,
              key: 'maxChoices',
              value: value,
            })
        "
        @increment="
          $store.commit('updateValue', {
            parent: question,
            key: 'maxChoices',
            value: parseInt(question.maxChoices) + 1,
          })
        "
        @decrement="
          $store.commit('updateValue', {
            parent: question,
            key: 'maxChoices',
            value: parseInt(question.maxChoices) - 1,
          })
        "
      />
    </div>
    <line-base class="dark" />
  </div>
</template>

<script>
import SurveyServices from "../../services/SurveyServices";

import LineBase from "./LineBase.vue";
import ToggleBase from "./ToggleBase.vue";
import TextBoxNum from "./TextBoxNum.vue";


export default {
  name: "PanelOptionsMultipleChoice",
  components: {
    ToggleBase,
    LineBase,
    TextBoxNum,
  },
  methods : {
    /**
     * Insert a new choice for multiple choice question and save
     */
    async insertNewElement(store) {
      const resp = await SurveyServices.postMultiChoiceQuestion(this.question.typedata.id, 
        {order: String(this.question.choices.length + 1), title: this.$t('app.MCDefault')})

      store.commit('insertLastElement', {
        list: this.question.choices,
        element: { text: this.$t('app.MCDefault'), ...resp},
      })
    },
    /**
     * Remove last choice from multiple choice question and save
     */
    async removeLastElement(store) {
      const temp_id = this.question.choices.slice(-1)[0].id
      store.commit('removeLastElement', this.question.choices)

      await SurveyServices.deleteMultiChoiceQuestion(this.question.typedata.id, {id: String(temp_id)})
    }
  },
  props: {
    question: Object,
  },
};
</script>

<style scoped>
html:lang(ur) * {
  text-align: right;
}

.close-header {
  padding-bottom: 0px;
}

h1,
h2 {
  color: black;
  padding: 0 16px;
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  text-align: left;
}

h1 {
  font-size: 16px;
  font-weight: bold;
  padding: 16px;
}

h2 {
  font-size: 16px;
  font-weight: bold;
}

.text-with-button {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  align-content: center;
}

label {
  width: 60px;
  line-height: 40px;
}
</style>