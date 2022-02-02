<template>
  <!-- Not Flow view - normal edit view -->
  <div v-if="!flowView" class="work-space">
    <div class="survey-title">
      <h1 contenteditable @focusout="handleTitleInput">
        {{ surveyTitle }}
      </h1>
    </div>
    <line-base class="light"></line-base>

    <button-base
      class="tertiary min"
      :icon="'fas fa-plus fa-sm'"
      :title="$t('workSpace.addNewBlock')"
      @buttonPress="$store.commit('insertNewBlock', { order: 1 })"
    ></button-base>

    <line-base class="light"></line-base>

    <div class="block-segment" v-for="block in sortedBlocks" :key="block.order">
      <builder-block :block="block" />
      <line-base class="light"></line-base>
      <button-base
        class="tertiary min"
        :icon="'fas fa-plus fa-sm'"
        :title="$t('workSpace.addNewBlock')"
        @buttonPress="
          $store.commit('insertNewBlock', { order: block.order + 1 })
        "
      ></button-base>
      <line-base class="light"></line-base>
    </div>
  </div>

  <!-- Flow view -->
  <div v-else class="work-space">
    <div class="survey-title">
      <h1>{{ surveyTitle }}</h1>
    </div>
    <line-base class="light"></line-base>

    <the-flow-editor />

  </div>
</template>


<script>
import SurveyServices from "../../services/SurveyServices";

import BuilderBlock from "./BuilderBlock.vue";
import ButtonBase from "../../components/ButtonBase.vue";
import LineBase from "./LineBase.vue";
import store from "../../store/SurveyBuilder";

import { mapGetters } from "vuex";
import TheFlowEditor from './TheFlowEditor.vue';

export default {
  name: "TheWorkSpace",
  store: store,
  components: {
    LineBase,
    ButtonBase,
    BuilderBlock,
    TheFlowEditor,
  },
  computed: {
    ...mapGetters(["surveyTitle", "editorData", "sortedBlocks", "flowView"]),
  },
  methods: {
    /**
     * Update survey title and send to backend
     * @param e - event
     */
    async handleTitleInput(e) {
      store.commit("updateSurveyTitle", e.target.innerHTML);

      // Really shouldn't hardcode which survey it is
      await SurveyServices.patchSurvey(store.state.survey.id, {name: e.target.innerHTML})
    },
  },
};
</script>

<style scoped>
html:lang(ur) * {
  text-align: right;
}

.work-space {
  background-color: #eff2f5;
  width: 100%;
  min-height: calc(100vh - 56px);
  overflow: scroll;

  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  padding: 16px;
  align-items: center;
}

.button-row {
  padding: 8px 8px 0px 8px;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
}

h1 {
  color: black;
  padding: 0 8px;
  font-family: Arial, Helvetica, sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  text-align: left;
}

.survey-title:hover > *[contenteditable="true"],
.survey-title:focus > *[contenteditable="true"] {
  background-color: white;
  outline: 0;
}

.survey-title > *[contenteditable="true"] {
  padding: 8px;
  border: 2px solid white;
  border-radius: 4px;
}

.text-with-button {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 100%;
  align-content: center;
}

.survey-title {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.block-segment {
  display: flex;
  flex-direction: column;
  justify-content: center;
  max-width: 816px;
  min-width: 816px;
  margin: 0 auto;
}
</style>
