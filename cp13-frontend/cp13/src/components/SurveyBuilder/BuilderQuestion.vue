<template>
  <div
    class="question"
    :class="isActiveQuestion ? 'active' : ''"
    @click="handleQuestionClick"
  >
    <div class="question-header">
      <div class="question-titles">
        <h1>
          Q{{ question.order }}
          <span class="required" v-if="question.required">*</span>
        </h1>
        <input
          type="text"
          v-model="question.title"
          @blur="updateQuestionTitle"
          class="question-title h2-tb"
          :style="$i18n.locale === 'ur' ? 'text-align: right;' : 'text-align: left;'"
        />
      </div>
      <div class="opt-container" >
        <div class="popup" 
          :style="$i18n.locale === 'ur' ? 'left: 0px;' : 'right: 0px;'" 
          :class="questionOptions ? 'show below' : ''"
        >
          <h3>{{ $t("builderQuestion.questionOptions") }}</h3>
          <line-base class="dark" />
          <ul>
            <li>
              <button-base
                class="secondary min"
                :icon="'fas fa-clone fa-me'"
                :title="$t('builderQuestion.duplicateQuestion')"
                @mousedown="
                  $store.commit('duplicateQuestion', {
                    block: block,
                    question: question,
                  })
                "
              />
            </li>
            <line-base class="dark" />
            <li>
              <button-base
                class="secondary min red"
                :title="$t('builderQuestion.deleteQuestion')"
                :icon="'fas fa-trash fa-me'"
                @mousedown="deleteQuestionFunc"
              />
            </li>
          </ul>
        </div>
        <button-base
          class="secondary square"
          :icon="'fas fa-ellipsis-h fa-lg'"
          @buttonPress="pressQuestionOptions"
          @buttonUnfocus="unfocusQuestionOptions"
        />
      </div>
    </div>

    <line-base class="light"></line-base>

    <h2 class="subtitle">
      {{ $t("builderQuestion.questionType") }}: {{ question.type }}
    </h2>
    <line-base class="light"></line-base>

    <!-- NEWS POST QUESTION -->
    <question-content-articles
      v-if="question.type === 'News post'"
      :data="question"
    />

    <!-- TEXT ENTRY QUESTION -->
    <div v-if="question.type === 'Text entry'" class="question-content">
      <h2>{{ $t("builderQuestion.textEntryPlaceholder") }}</h2>

      <input
        type="text"
        v-model="question.query"
        @blur="inputTextboxQuestion"
      />
    </div>

    <!-- BUTTON ROW QUESTION -->
    <div v-if="question.type === 'Button row'" class="question-content">
      <h2>{{ $t("builderQuestion.buttonContent") }}</h2>
      <div
        v-for="button in question.buttons"
        :key="question.buttons.indexOf(button)"
        class="question-titles"
      >
        <h1>{{ question.buttons.indexOf(button) + 1 }}.</h1>
        <input
          type="text"
          v-model="question.buttons[question.buttons.indexOf(button)].text"
          @blur="
            (input) =>
              inputTextboxButton(
                question.buttons[question.buttons.indexOf(button)]
              )
          "
        />
      <h2 v-if="question.terminating" >{{ $t("builderQuestion.endSelected") }}</h2>
      <button v-if="question.terminating" class="custom-checkbox" @click="inputTerminatesButton(question.buttons[question.buttons.indexOf(button)])">
        <i v-if="button.terminates" class="fa fa-check fa-lg"></i>
      </button>
      </div>
    </div>

    <!-- MULTIPLE CHOICE QUESTION -->
    <div v-if="question.type === 'Multiple choice'" class="question-content">
      <h2>{{ $t("builderQuestion.multipleChoiceOptions") }}</h2>
      <div
        v-for="choice in question.choices"
        :key="question.choices.indexOf(choice)"
        class="question-titles"
      >
        <h1>{{ question.choices.indexOf(choice) + 1 }}.</h1>
        <input
          type="text"
          style="width: 100%"
          v-model="question.choices[question.choices.indexOf(choice)].text"
          @blur="
            (input) =>
              inputTextboxMultichoice(
                question.choices[question.choices.indexOf(choice)]
              )
          "
        />
      </div>
    </div>

    <!-- Drag and Drop -->
    <div v-if="question.type === 'Drag and Drop'" class="question-content">
      <h2>{{ $t("builderQuestion.DnDChips") }}</h2>
      <div
        v-for="choice in question.choices"
        :key="question.choices.indexOf(choice) + ' Chip'"
        class="question-titles"
      >
        <h1>{{ question.choices.indexOf(choice) + 1 }}.</h1>

        <input
          type="text"
          style="width: 100%"
          v-model="question.choices[question.choices.indexOf(choice)].text"
          @unfocus="
            (input) =>
              $store.commit('updateValue', {
                parent: question.choices[question.choices.indexOf(choice)],
                key: 'text',
                value: input,
              })
          "
        />
      </div>

      <line-base class="light" />
      
      <h2>{{ $t("builderQuestion.DnDCategories") }}</h2>
      <div
        v-for="category in question.categories"
        :key="question.categories.indexOf(category)"
        class="question-titles"
      >
        <h1>{{ question.categories.indexOf(category) + 1 }}.</h1>

        <input
          type="text"
          style="width: 100%"
          v-model="
            question.categories[question.categories.indexOf(category)].text
          "
          @unfocus="
            (input) =>
              $store.commit('updateValue', {
                parent:
                  question.categories[question.categories.indexOf(category)],
                key: 'text',
                value: input,
              })
          "
        />
      </div>
    </div>

    <!-- NUMBER SCALE QUESTION -->
    <div v-if="question.type === 'Number scale'" class="question-content">
      <div v-if="question.minTitleOn">
        <h2>{{ $t("builderQuestion.minTitle") }}</h2>

        <input
          type="text"
          v-model="question.minTitle"
          @blur="inputMinLabelNumberScale"
        />
      </div>
      <div v-if="question.midTitleOn">
        <h2>{{ $t("builderQuestion.midTitle") }}</h2>

        <input
          type="text"
          v-model="question.midTitle"
          @blur="inputMidLabelNumberScale"
        />
      </div>
      <div v-if="question.maxTitleOn">
        <h2>{{ $t("builderQuestion.maxTitle") }}</h2>

        <input
          type="text"
          v-model="question.maxTitle"
          @blur="inputMaxLabelNumberScale"
        />
      </div>
      <line-base
        class="light"
        v-if="question.minTitleOn || question.midTitleOn || question.maxTitleOn"
      />

      <h2 style="text-align: center">
        {{ $t("builderQuestion.livePreview") }}
      </h2>
      <div class="scale-labels">
        <p>{{ question.minTitleOn ? question.minTitle : "" }}</p>
        <p>{{ question.midTitleOn ? question.midTitle : "" }}</p>
        <p>{{ question.maxTitleOn ? question.maxTitle : "" }}</p>
      </div>
      <div class="scale-blocks">
        <div v-for="b in getScaleList()" :key="b" class="scale-block">
          <h1>{{ b }}</h1>
        </div>
      </div>
    </div>
  </div>
</template> 


<script>
import SurveyServices from "../../services/SurveyServices";

import ButtonBase from "../../components/ButtonBase.vue";
import LineBase from "./LineBase.vue";
import TextBox from "./TextBox.vue";
import QuestionContentArticles from "./QuestionContentArticles.vue";

import store from "../../store/SurveyBuilder.js";

export default {
  name: "BuilderQuestion",
  store: store,
  components: {
    ButtonBase,
    LineBase,
    TextBox,
    QuestionContentArticles,
  },
  props: {
    block: Object,
    blockOrder: Number,
    currentQuestion: Number,
    question: Object,
  },
  data: function () {
    return { questionOptions: false };
  },
  methods: {
    /**
     * Update and save question title
     */
    async updateQuestionTitle() {
      await SurveyServices.patchQuestion(this.question.id, { name: this.question.title });
    },
    /**
     * Handle question being clicked
     */
    handleQuestionClick() {
      store.commit("handleQuestionClick", {
        questionOrder: this.question.order,
        blockOrder: this.blockOrder,
      });
    },
    /**
     * Delete a question from a block
     */
    deleteQuestionFunc() {
      store.commit("deleteQuestion", {
        block: this.block,
        question: this.question,
      });
    },
    /**
     * Display popup for question options
     */
    pressQuestionOptions() {
      this.questionOptions = !this.questionOptions;
    },
    /**
     * Hide popup for question options
     */
    unfocusQuestionOptions() {
      this.questionOptions = false;
    },
    /**
     * Save text entry question query
     */
    async inputTextboxQuestion() {
      await SurveyServices.patchQuestionType(this.question.id, {
        query: this.question.query,
      });
    },
    /**
     * Save min label number scale query
     */
    async inputMinLabelNumberScale() {
      store.commit('updateValue', {
        parent: this.question,
        key: 'minTitle',
        value: this.question.minTitle,
      })

      await SurveyServices.patchQuestionType(this.question.id, {
        minTitle: this.question.minTitle,
      });
    },
    /**
     * Save max label number scale query
     */
    async inputMaxLabelNumberScale() {
      store.commit('updateValue', {
        parent: this.question,
        key: 'maxTitle',
        value: this.question.maxTitle,
      })

      await SurveyServices.patchQuestionType(this.question.id, {
        maxTitle: this.question.maxTitle,
      });
    },
    /**
     * Save mid label number scale query
     */
    async inputMidLabelNumberScale() {
      store.commit('updateValue', {
        parent: this.question,
        key: 'midTitle',
        value: this.question.midTitle,
      })

      await SurveyServices.patchQuestionType(this.question.id, {
        middleTitle: this.question.midTitle,
      });
    },
    /**
     * Save multiple choice option text
     */
    async inputTextboxMultichoice(choice) {     
      await SurveyServices.patchMultiChoiceQuestion(this.question.typedata.id, {
        id: choice.id,
        title: this.question.choices[this.question.choices.indexOf(choice)].text,
      });
    },
    /**
     * Save button text in button
     */
    async inputTextboxButton(button) {
      await SurveyServices.patchButtonRowQuestion(this.question.typedata.id, {
        id: button.id,
        buttonText: this.question.buttons[this.question.buttons.indexOf(button)].text
      });
    },
    async inputTerminatesButton(button) {
      store.commit('toggle', { 
        parent: button, 
        key: 'terminates' 
      })

      console.log("Terminates: ", button.terminates)
      await SurveyServices.patchButtonRowQuestion(this.question.typedata.id, {
        id: button.id,
        goToEnd: button.terminates
      });
    },
    /**
     * Create list for number scale
     * @returns number scale list
     */
    getScaleList() {
      let list = [];
      for (
        let i = this.question.minNum;
        i <= this.question.maxNum;
        i += this.question.interval
      ) {
        list.push(i);
      }
      return list;
    },
  },
  computed: {
    /**
     * Check if current question is selected
     * @returns true if is selected and false otherwise
     */
    isActiveQuestion: function () {
      if (this.currentQuestion == this.question.order) {
        return true;
      }

      return false;
    },
  },
};
</script>

<style scoped lang="scss">
@import "./src/assets/textbox.scss";

html:lang(ur) * {
  text-align: right;
}

.custom-checkbox {
    display: inline-block;
    min-height: 36px;
    max-height: 36px;
    max-width: 36px;
    min-width: 36px;
    border-radius: 4px;
    text-align: center;
    font-size: 1em;
    border: 2px solid black;
    background: white;
    margin-right: 8px;
    padding: 0;
    color: green;

}

.scale-blocks,
.scale-labels {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  overflow: scroll;
}

.scale-block {
  text-align: center;
  background-color: #eff2f5;
  border-radius: 8px;
  margin: 2px;
  flex-grow: 1;
  justify-content: center;
  display: flex;
}

.subtitle {
  text-align: left;
  color: #566370;
}

.question {
  display: flex;
  flex-direction: column;
  background-color: white;
  margin: 8px;
  border-radius: 8px;
  border-width: 2px;
  border-style: solid;
  padding: 8px;
  border-color: #eff2f5;
}

.question:hover {
  border-color: #566370;
}

.active,
.question.active:hover {
  border-color: #1947e5;
}

h1,
h2 {
  color: black;
  padding: 0 0 0 8px;
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  font-weight: bold;
  text-align: left;
  margin-right: 8px;
}

h1 {
  font-size: 24px;
}

h2 {
  font-size: 16px;
}

.required {
  color: red;
}

.question-header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.question-titles {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  width: 100%;
  white-space: nowrap;

}

.question-title {
  width: calc(100% - 100px);
  margin-right: 8px;
}

.button-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
}

.question-titles:hover > *[contenteditable="true"],
.question-titles:focus > *[contenteditable="true"] {
  border: 2px solid #566370;
}

.question-titles > *[contenteditable="true"] {
  padding: 8px;
  border: 2px solid #eff2f5;
  border-radius: 4px;
}

/* Popup styling */
.opt-container {
  position: relative;
  display: flex;
  justify-content: right;
}

.popup {
  position: absolute;

  z-index: 2;
  display: none;

  width: 300px;
  margin: 0 auto;
  border: 2px solid #566370;
  border-radius: 8px;
  padding: 0 8px;
  background-color: #eff2f5;
}

.below {
  top: 62px;
}

.show {
  display: block;
}

.popup ul,
.popup ul li {
  list-style-type: none;
  margin: 0;
  padding: 0;
  align-items: center;
}

.popup ul li button {
  width: 100%;
  margin: 8px auto;
}

.popup h3 {
  text-align: left;
  padding: 0 8px;
}
/* End of popup styling */
</style>
