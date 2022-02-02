<template>
  <div class="options">
    <div class="text-with-button">
      <h2>{{ $t("pOptionsTextEntry.validateAnswer") }}</h2>
      <toggle-base
        :toggled="question.validation"
        @handleToggle="
          $store.commit('toggle', { parent: question, key: 'validation' })
        "
      ></toggle-base>
    </div>
    <div v-if="question.validation">
      <line-base class="light" />
      <h1 class="close-header">{{ $t("pOptionsTextEntry.answerType") }}</h1>
      <dropdown-base
        :options="['Text', 'Integer', 'Decimal']"
        :currentType="question.answerType"
        @input="handleTextAnswerType"
        class="secondary-drop"
      />
      <line-base class="light" />
      <h1 v-if="question.answerType === 'Text'" class="close-header">{{ $t("pOptionsTextEntry.minCharLength") }} </h1>
      <h1 v-else-if="question.answerType === 'Integer'" class="close-header">{{ $t("pOptionsTextEntry.intLowerBound") }}</h1>
      <h1 v-else class="close-header">{{ $t("pOptionsTextEntry.decLowerBound") }}</h1>
      <text-box-num
        :placeholder="$t('pOptionsTextEntry.minPlaceholder')"
        :value="question.textBoxMin != null ? question.textBoxMin.toString() : null"
        :key="question.textBoxMin"
        @update="
          (value) =>
            $store.commit('updateValue', {
              parent: question,
              key: 'textBoxMin',
              value: value,
            })
        "
        @increment="
          $store.commit('updateValue', {
            parent: question,
            key: 'textBoxMin',
            value: parseInt(question.textBoxMin) + 1,
          })
        "
        @decrement="
          $store.commit('updateValue', {
            parent: question,
            key: 'textBoxMin',
            value: parseInt(question.textBoxMin) - 1,
          })
        "
      />
      <line-base class="light" />
      <h1 v-if="question.answerType === 'Text'" class="close-header">{{ $t("pOptionsTextEntry.maxCharLength") }}</h1>
      <h1 v-else-if="question.answerType === 'Integer'" class="close-header">{{ $t("pOptionsTextEntry.intUpperBound") }}</h1>
      <h1 v-else class="close-header">{{ $t("pOptionsTextEntry.decUpperBound") }}</h1>
      <text-box-num
        :placeholder="$t('pOptionsTextEntry.maxPlaceholder')"
        :value="question.textBoxMax != null ? question.textBoxMax.toString() : null"
        :key="question.textBoxMax"

        @update="
          (value) =>
            $store.commit('updateValue', {
              parent: question,
              key: 'textBoxMax',
              value: value,
            })
        "
        @increment="
          $store.commit('updateValue', {
            parent: question,
            key: 'textBoxMax',
            value: parseInt(question.textBoxMax) + 1,
          })
        "
        @decrement="
          $store.commit('updateValue', {
            parent: question,
            key: 'textBoxMax',
            value: parseInt(question.textBoxMax) - 1,
          })
        "
      />
    </div>
    <line-base class="dark" />
  </div>
</template>

<script>
import LineBase from "./LineBase.vue";
import ToggleBase from "./ToggleBase.vue";
import TextBoxNum from "./TextBoxNum.vue";
import DropdownBase from "./DropdownBase.vue";
import store from "../../store/SurveyBuilder.js";

export default {
  name: "PanelOptionsTextEntry",
  store: store,
  components: {
    ToggleBase,
    LineBase,
    TextBoxNum,
    DropdownBase,
  },
  props: {
    question: Object,
  },
  methods: {
    /**
     * Handle text entry question answer type being changed in dropdown
     * @param data - data provided by dropdown
     */
    handleTextAnswerType(data) {
      store.commit("handleTextAnswerType", {
        question: this.question,
        ansType: data.options[data.index],
      });
    },
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